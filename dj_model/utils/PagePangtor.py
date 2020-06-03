import copy


class Pagination(object):
    def __init__(self, request, current_page, all_data_num, each_page_data_num=1, max_page_num=3):
        # 封装页面相关数据
        '''
        current_page:当前页
        data_num:数据总条数
        each_page:每页数据条数
        max_page_num:最大显示的页码数
        page_num: 总页数
       '''
        self.url_data = copy.deepcopy(request.GET)

        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        if current_page < 1:
            current_page = 1

        self.current_page = current_page
        self.all_data_num = all_data_num  # 100
        self.each_page_data_num = each_page_data_num  #
        self.max_page_num = max_page_num  # 总大显示的页码数
        # 计算总页数
        total_page_num, tmp = divmod(self.all_data_num, self.each_page_data_num)
        if tmp:
            total_page_num += 1
        self.total_page_num = total_page_num  # 总页数

        self.page_count_half = int((self.max_page_num - 1) / 2)

    @property
    def start(self):
        return (self.current_page - 1) * self.each_page_data_num

    @property
    def end(self):
        return self.current_page * self.each_page_data_num

    def page_html(self):
        # 总页码 < 最大显示的页码数
        if self.total_page_num < self.max_page_num:
            page_start = 1
            page_end = self.total_page_num + 1

        # 总页码 > 最大显示的页码数
        else:

            if self.current_page <= self.page_count_half:
                page_start = 1
                page_end = self.max_page_num + 1
            elif (self.current_page + self.page_count_half) > self.total_page_num:
                page_start = self.total_page_num - self.max_page_num + 1
                page_end = self.total_page_num + 1
            else:
                page_start = self.current_page - self.page_count_half
                page_end = self.current_page + self.page_count_half + 1

        page_html_lst = []

        # 首页，上一页标签
        self.url_data["page"] = 1
        frist_page = '<nav aria-label="Page navigation example"><ul class="pagination"><li class="page-item disabled"><a href="#" class="page-link">共 '+str(self.all_data_num)+'条，'+str(self.total_page_num)+' 页</a></li> <li class="page-item"><a href="?%s" class="page-link">首页</a></li>' % (
            self.url_data.urlencode(),)
        page_html_lst.append(frist_page)
        self.url_data["page"] = self.current_page - 1
        if self.current_page <= 1:
            prev_page = '<li class="page-item disabled"><a href="#" class="page-link">上一页</a></li>'
        else:
            prev_page = '<li class="page-item"><a href="?%s" class="page-link">上一页</a></li>' % (
                self.url_data.urlencode(),)
        page_html_lst.append(prev_page)

        # 每页显示的页码

        for i in range(page_start, page_end):
            self.url_data["page"] = i
            if i == self.current_page:
                tmp = '<li class="page-item active" aria-current="page"><a href="?%s" class="page-link" style="color:white">%s</a></li>' % (
                    self.url_data.urlencode(), i,)
            else:
                tmp = '<li class="page-item"><a href="?%s" class="page-link">%s</a></li>' % (
                    self.url_data.urlencode(), i,)
            page_html_lst.append(tmp)

        self.url_data["page"] = self.current_page + 1
        if self.current_page >= self.total_page_num:
            next_page = '<li class="page-item disabled"><a href="#" class="page-link">下一页</a></li>'
        else:
            next_page = '<li class="page-item"><a href="?%s" class="page-link">下一页</a></li>' % (
                self.url_data.urlencode(),)
        page_html_lst.append(next_page)
        self.url_data["page"] = self.total_page_num
        last_page = '<li class="page-item"><a href="?%s" class="page-link">尾页</a></li></ul></nav>' % (
            self.url_data.urlencode(),)
        page_html_lst.append(last_page)
        if self.all_data_num==0:
            page_html_lst= ['<nav aria-label="Page navigation example"><ul class="pagination"><li>没有查到数据~~</li></ul></nav>']
        return "".join(page_html_lst)


    def page_html_2_dialog(self):
        # 总页码 < 最大显示的页码数
        if self.total_page_num < self.max_page_num:
            page_start = 1
            page_end = self.total_page_num + 1

        # 总页码 > 最大显示的页码数
        else:

            if self.current_page <= self.page_count_half:
                page_start = 1
                page_end = self.max_page_num + 1
            elif (self.current_page + self.page_count_half) > self.total_page_num:
                page_start = self.total_page_num - self.max_page_num + 1
                page_end = self.total_page_num + 1
            else:
                page_start = self.current_page - self.page_count_half
                page_end = self.current_page + self.page_count_half + 1

        page_html_lst = []

        # 首页，上一页标签
        self.url_data["page"] = 1
        frist_page = '<nav aria-label="Page navigation example"><ul class="pagination"><li class="page-item disabled"><a href="javaScript:goPage(1)" class="page-link">共 '+str(self.all_data_num)+'条，'+str(self.total_page_num)+' 页</a></li> <li class="page-item"><a href="javaScript:goPage(1)" class="page-link">首页</a></li>'
        page_html_lst.append(frist_page)
        self.url_data["page"] = self.current_page - 1
        if self.current_page <= 1:
            prev_page = '<li class="page-item disabled"><a href="#" class="page-link">上一页</a></li>'
        else:
            prev_page = '<li class="page-item"><a href="javaScript:goPage(%s)" class="page-link">上一页</a></li>' % (
                self.current_page-1,)
        page_html_lst.append(prev_page)

        # 每页显示的页码

        for i in range(page_start, page_end):
            self.url_data["page"] = i
            if i == self.current_page:
                tmp = '<li class="page-item active" aria-current="page"><a href="javaScript:goPage(%s)" class="page-link" style="color:white">%s</a></li>' % (
                    i, i,)
            else:
                tmp = '<li class="page-item"><a href="javaScript:goPage(%s)" class="page-link">%s</a></li>' % (
                    i, i,)
            page_html_lst.append(tmp)

        self.url_data["page"] = self.current_page + 1
        if self.current_page >= self.total_page_num:
            next_page = '<li class="page-item disabled"><a href="#" class="page-link">下一页</a></li>'
        else:
            next_page = '<li class="page-item"><a href="javaScript:goPage(%s)" class="page-link">下一页</a></li>' % (
                self.current_page+1,)
        page_html_lst.append(next_page)
        self.url_data["page"] = self.total_page_num
        last_page = '<li class="page-item"><a href="javaScript:goPage(%s)" class="page-link">尾页</a></li></ul></nav>' % (
            self.total_page_num,)
        page_html_lst.append(last_page)
        if self.all_data_num == 0:
            page_html_lst= ['<nav aria-label="Page navigation example"><ul class="pagination"><li>没有查到数据~~</li></ul></nav>']
        return "".join(page_html_lst)
