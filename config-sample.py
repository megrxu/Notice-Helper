from core.parser import parse_rss, parse_college, parse_cspo, parse_math, parse_cse

# URLs

urls = [
    {
        'name': '信电学院',
        'link': 'http://www.isee.zju.edu.cn/notice/',
        'parser': parse_college
    }, {
        'name': '竺可桢学院',
        'link': 'http://ckc.zju.edu.cn/office/',
        'parser': parse_college
    }, {
        'name': '计算机学院',
        'link': 'http://cspo.zju.edu.cn/',
        'parser': parse_cspo
    }, {
        'name': '数学科学学院',
        'link': 'http://www.math.zju.edu.cn/',
        'parser': parse_math
    }, {
        'name': '控制学院',
        'link': 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1',
        'parser': parse_cse
    },]
