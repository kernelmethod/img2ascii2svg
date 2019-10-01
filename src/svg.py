"""
Code for converting ASCII art to SVG format.
"""

"""
Globals
"""
###
### Javascript code to inject into the SVGs to ensure consistent size
###
# JS to ensure that bounding rectangle fits the text
RECTANGULAR_SVG_JS_INJECT = """\
window.addEventListener('load',function() {
    var bounding_rect = document.getElementById("bounding-rect");
    var text = document.getElementById("ascii");
    var bb_text = text.getBBox();

    // Change the rectangle size to fit the text
    bounding_rect.setAttribute("width", bb_text.width);
    bounding_rect.setAttribute("height", bb_text.height);
}, false);"""

# JS to make text element square
SQUARE_SVG_JS_INJECT = """\
window.addEventListener('load',function() {
    var bounding_rect = document.getElementById("bounding-rect");
    var text = document.getElementById("ascii");
    var bb_text = text.getBBox();

    // Change the font size so that the height and width match up
    var font_size = Math.round(1e3 * bb_text.height / bb_text.width) / 1e3;
    text.setAttribute("font-size", font_size + "px");

    // Adjust size of bounding rectangle
    bb_text = text.getBBox();
    bounding_rect.setAttribute("width", bb_text.width);
    bounding_rect.setAttribute("height", bb_text.height);
}, false);"""

"""
ASCII -> SVG conversion
"""


def ascii_to_svg(txt):
    """
    Takes an ASCII text string and converts it into an SVG image.
    """
    # Do a search-and-replace for characters that will create rendering
    # isssues.
    txt = txt.replace("&", "&amp;")
    txt = txt.replace('"', "&quot;")
    txt = txt.replace("<", "&lt;")
    txt = txt.replace(">", "&gt;")
    # txt = txt.replace(" ", "&#160;")

    lines = txt.split("\n")
    width = len(lines[0])
    height = len(lines)

    svg_start = f"""\
<?xml version="1.0" encoding="UTF-8" ?>
<svg xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 {height} {height}"
        style="width: 100%; height: 100%; overflow: auto;">
    <script type="text/javascript"><![CDATA[
{SQUARE_SVG_JS_INJECT}
    ]]></script>
    <style type="text/css">
    text.ascii-art {{
        user-select: none;
        whiteSpace: "pre";
        fill: white;
        -webkit-user-select:none;
        -khtml-user-select:none;
        -moz-user-select:none;
        -ms-user-select:none;
    }}
    </style>
    <rect x="0" y="0" height="100%" width="100%" id="bounding-rect"/>
    <text x="0" y="0" id="ascii" font-family="monospace, courier" text-anchor="start"
        font-size="1px" class="ascii-art">
    """

    svg_middle = ""
    svg_end = """\
    </text>
</svg>"""

    # Add <tspan> elements in the middle
    dy = round(100 / len(lines), 3)
    for (ii, line) in enumerate(lines):
        start = """<tspan x="0" dy="%.3f%%" textLength="100%%" xml:space="preserve">""" % dy
        end = "</tspan>"
        svg_middle += start + line + end + "\n"

    return svg_start + svg_middle + svg_end
