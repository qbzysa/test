import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter_cases = "abcdefghjkmnpqrstuvwxy"                      # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()                          # 大写字母
_numbers = ''.join(map(str, range(10)))                       # 数字
# 初始化字符
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))


class Validate_Code(object):
    """
        @param size: 图片的大小，格式（宽，高），默认为(180, 30)
        @param chars: 允许的字符集合，格式字符串
        @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
        @param mode: 图片模式，默认为RGB
        @param bg_color: 背景颜色，默认为白色
        @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
        @param font_size: 验证码字体大小
        @param font_type: 验证码字体的详细路径，默认为 'arial.ttf'
        @param length: 验证码字符个数
        @param draw_lines: 是否划干扰线
        @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
        @param draw_points: 是否画干扰点
        @param point_chance: 干扰点出现的概率，大小范围[0, 100]
        """
    def __init__(self,
                 size=(200, 40),
                 chars=init_chars,
                 img_type="GIF",
                 mode="RGB",
                 bg_color=(230, 230, 230),
                 fg_color=(0, 0, 255),
                 font_size=20,
                 font_type='arial.ttf',
                 length=6,
                 draw_lines=True,
                 n_lines=(1, 2),
                 draw_points=True,
                 point_chance=1):

        self.size = size
        self.chars = chars
        self.img_type = img_type
        self.mode = mode
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font_size = font_size
        self.font_type = font_type
        self.length = length
        self.draw_lines = draw_lines
        self.n_line = n_lines
        self.draw_points = draw_points
        self.point_chance = point_chance
        self.width, self.height = self.size                             # 宽， 高
        self.code_img = Image.new(self.mode, self.size, self.bg_color)  # 创建图形
        self.draw = ImageDraw.Draw(self.code_img)                       # 创建画笔

    def get_chars(self):
        """
        生成给定长度的字符串，返回列表格式
        """
        return random.sample(self.chars, self.length)

    def create_lines(self):
        """
        绘制干扰线
        """
        line_num = random.randint(*self.n_line)  # 干扰线条数

        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            # 结束点
            end = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            self.draw.line([begin, end], fill=(0, 0, 0))

    def create_points(self):
        """
        绘制干扰点
        """
        chance = min(100, max(0, int(self.point_chance)))  # 大小限制在[0, 100]

        for w in range(self.width):
            for h in range(self.height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    self.draw.point((w, h), fill=(0, 0, 0))

    def create_strs(self):
        """
        绘制验证码字符
        """
        c_chars = self.get_chars()
        code = '%s' % ' '.join(c_chars)  # 每个字符前后以空格隔开
        font = ImageFont.truetype(self.font_type, self.font_size, encoding="utf-8")
        font_width, font_height = font.getsize(code)

        self.draw.text(((self.width-font_width)/3, (self.height-font_height)/3), code, font=font, fill=self.fg_color)

        return ''.join(c_chars)

    def create_validate_code(self):
        """
        生成PIL Image实例及验证码图片中的字符串
        :return:
              code_img : PIL Image实例
              code : 验证码图片中的字符串
        """
        if self.draw_lines:
            self.create_lines()
        if self.draw_points:
            self.create_points()
        code = self.create_strs()

        # 图形扭曲参数
        params = [1-float(random.randint(1, 2))/100, 0, 0, 0, 1-float(random.randint(1, 10))/100,
                  float(random.randint(1, 2))/500, 0.001, float(random.randint(1, 2))/500]
        code_img = self.code_img.transform(self.size, Image.PERSPECTIVE, params)  # 创建扭曲

        code_img = code_img.filter(ImageFilter.EDGE_ENHANCE_MORE)       # 滤镜，边界加强（阈值更大）
        return code_img, code


if __name__ == '__main__':
    val_code = Validate_Code()
    img, text = val_code.create_validate_code()
    print(text)
    # 生成验证码图片
    img.save('./code.gif', val_code.img_type)
