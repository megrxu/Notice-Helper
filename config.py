from core.parser import parse_rss, parse_college, parse_cspo, parse_cse

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
        'parser': parse_college
    }, {
        'name': '控制学院',
        'link': 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1',
        'parser': parse_cse
    }, {
        'name': '经济学院',
        'link': 'http://www.cec.zju.edu.cn/',
        'parser': parse_college
    }, {
        'name': '心理与行为科学系',
        'link': 'http://www.psych.zju.edu.cn/',
        'parser': parse_college
    }, {
        'name': '地球科学学院',
        'link': 'http://gs.zju.edu.cn/redir.php?catalog_id=2',
        'parser': parse_college
    }, {
        'name': '能源工程学院',
        'link': 'http://www.doe.zju.edu.cn/',
        'parser': parse_college
    }, {
        'name': '海洋学院',
        'link': 'http://10.77.12.12/office/redir.php?catalog_id=39644',
        'parser': parse_college
    }, {
        'name': '航空航天学院',
        'link': 'http://saa.zju.edu.cn/office/',
        'parser': parse_college
    }, {
        'name': '光电科学与工程学院',
        'link': 'http://opt.zju.edu.cn/index.php',
        'parser': parse_college
    }, {
        'name': '生命科学学院',
        'link': 'http://www.cls.zju.edu.cn/redir.php?catalog_id=97797',
        'parser': parse_college
    }, {
        'name': '生物系统工程与食品科学学院',
        'link': 'http://www.caefs.zju.edu.cn/office/',
        'parser': parse_college
    }]
