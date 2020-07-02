from fdfs_client.client import *
from concurrent.futures import ThreadPoolExecutor
from Aiplatform.settings import *

# def get_tracker_conf(conf_path=r'E:\workdir\MUYUAN\ai_plat_dj\my-ai-aiplatform\Aiplatform\database_label\utils\client.conf'):
#     cf = Fdfs_ConfigParser()
#     tracker = {}
#     try:
#         cf.read(conf_path)
#         print(cf.read(conf_path), '??')
#         timeout = cf.getint('__config__', 'connect_timeout')
#         tracker_list = cf.get('__config__', 'tracker_server')
#         if isinstance(tracker_list, str):
#             tracker_list = [tracker_list]
#         tracker_ip_list = []
#         for tr in tracker_list:
#             tracker_ip, tracker_port = tr.split(':')
#             tracker_ip_list.append(tracker_ip)
#         tracker['host_tuple'] = tuple(tracker_ip_list)
#         tracker['port'] = int(tracker_port)
#         tracker['timeout'] = timeout
#         tracker['name'] = 'Tracker Pool'
#     except:
#         raise
#     return tracker


class MyFdfs(object):
    def __init__(self):

        self.client_conf = get_tracker_conf(FDFS_CONF_PATH)
        self.client = Fdfs_client(self.client_conf)


    @classmethod
    def upload_(cls, file):
        """
        :param file: list of bytes file
        :return:
        """
        try:
            res = cls().client.upload_by_buffer(file)
            file_detail = {'upload_status': res['Status'],
                           'file_id': res['Remote file_id'].decode()
                           } if res['Status'] == 'Upload successed.' else {'upload_status':res['Status']}
        except Exception as e:
            return e
        return file_detail

    @classmethod
    def upload_suf(cls, file, suf):
        """
        :param file: list of bytes file
        :return:
        """
        try:
            res = cls().client.upload_by_buffer(file,file_ext_name=suf)
            file_detail = {'upload_status': res['Status'],
                           'file_id': res['Remote file_id'].decode()
                           } if res['Status'] == 'Upload successed.' else {'upload_status': res['Status']}
        except Exception as e:
            return e
        return file_detail
        # if upload to Fdfs successfully
        # try:
        #     # upload to mysql
        #     f_name = file.name     # unique name  if not exists
        #     pass
        # except Exception as e:
        #     return 0

        # # 测试用
        # with open(file, 'rb') as f:
        #     f = f.read()
        #     res = cls().client.upload_by_buffer(f)
        #     file_id = res['Remote file_id'] if res['Status'] == 'Upload successed.' else 'upload faild'
        # return file_detail

    @classmethod
    def download_(cls, name, remote_file_id):
        remote_file_id = bytes(remote_file_id, encoding='utf-8')
        try:
            ret = cls().client.download_to_buffer(remote_file_id)
            bytes_file =  ret['Content'] if ret['Content'] else 0
            return bytes_file
        except Exception as e:
            return 0

    @classmethod
    def delete_(cls, remote_file_id):
        remote_file_id = bytes(remote_file_id, encoding='utf-8')
        try:
            ret = cls().client.delete_file(remote_file_id)
            return ret
        except Exception as e:
            return e

# 通过bytes写入
    @classmethod
    def write_(cls, remote_file_id):
        remote_file_id = bytes(remote_file_id, encoding='utf-8')
        try:
            ret = cls().client.delete_file(remote_file_id)
            return 1
        except Exception as e:
            return e

    @staticmethod
    def upload(upload_list:list):
        """

        :param upload_list: [{'file': bytes 文件1, 'file_name':'file_name_1'}, {'file': bytes 文件1, 'file_name':'file_name_1'}]
        :return:
        """

        with ThreadPoolExecutor(max_workers=2) as excutor:
            tasks = [excutor.submit(MyFdfs.upload_, i).result() for i in upload_list]
        return tasks

    @staticmethod
    def upload_sufs(upload_list: list):
        """

        :param upload_list: [{'file': bytes 文件1, 'file_name':'file_name_1'}, {'file': bytes 文件1, 'file_name':'file_name_1'}]
        :return:
        """

        with ThreadPoolExecutor(max_workers=2) as excutor:
            # tasks = [excutor.submit(MyFdfs.upload_suf, i).result() for i in upload_list]
            tasks = excutor.submit(MyFdfs.upload_suf, upload_list[0], upload_list[1]).result()
        return tasks

    @staticmethod
    def download(download_list:list):   # {'tttttest1.txt': "b'group1/M00/00/00/wKgZgF6yiyeAG5XhAAAALWvVllI261.txt'"}
        """
        get a list of bytes style file and packaged whatever u want
        :param download_list: list 0f remote_id
        :return: list of bytes style
        """
        with ThreadPoolExecutor(max_workers=2) as excutor:
            for download_dict in download_list:
                tasks = [excutor.submit(MyFdfs.download_, name, remote_ip).result() for name, remote_ip in download_dict.items()]
        return tasks

    @staticmethod
    def delete_file(id_list):
        with ThreadPoolExecutor(max_workers=2) as excutor:
            tasks = [excutor.submit(MyFdfs.delete_, remote_ip).result() for remote_ip in id_list]
        return tasks

    # @staticmethod
    # def write_in(content:bytes):
    #     with ThreadPoolExecutor(max_workers=2) as excutor:
    #         pass
    #     return 'ok'