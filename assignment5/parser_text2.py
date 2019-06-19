from parser import parse_downmark


"""
Used this file to check if the parser.py would work, in 5.2.

Simply just run

$ python parser_text2.py

in terminal.
"""


def verify(function, inputs, outputs):
    for sample_input, expected_output in zip(inputs, outputs):
        actual_output = function(sample_input)
        try:
            assert actual_output == expected_output
        except AssertionError:
            print(
                (
                    "Something seems to be wrong with your code! On the input:\n{}\n"
                    "it should have returned:\n{}\nbut returned:\n{}\n instead!"
                ).format(sample_input, expected_output, actual_output)
            )

  
sample_input = """
%Lorem% ipsum *dolor sit amet*, consectetur *adipiscing elit. Nullam tempor* nunc at justo tincidunt congue. %Aliquam hendrerit mollis pretium! Praesent id% mi est. [Praesent,](www.praesent.com) sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

>>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla *eget eros euismod volutpat. Suspendisse* id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat %molestie \*libero vel\%\% pulvinar? Sed% a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.

Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in \%% urna. \% Fusce% in *sapien %mau\*ris.% Duis purus dui*, viverra in tellus eu, imperdiet fringilla [felis. Curabitur rhoncus tincidunt varius. Cras](inf3331.no) gravida metus ut [wp:vestibulum] vestibulum. \*Integer cursus* ex\* in rutrum volutpat*. Nunc scelerisque gravida risus sed ullamcorper. Proin [lorem,](https://www.malesuada.com) massa <https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif>(w=100,h=40) quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio *bibendum.*
"""

expected_output = """
<b>Lorem</b> ipsum <i>dolor sit amet</i>, consectetur <i>adipiscing elit. Nullam tempor</i> nunc at justo tincidunt congue. <b>Aliquam hendrerit mollis pretium! Praesent id</b> mi est. <a href='http://www.praesent.com'>Praesent,</a> sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

<blockquote>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla <i>eget eros euismod volutpat. Suspendisse</i> id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat <b>molestie *libero vel%% pulvinar? Sed</b> a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.</blockquote>

Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in %<b> urna. % Fusce</b> in <i>sapien <b>mau*ris.</b> Duis purus dui</i>, viverra in tellus eu, imperdiet fringilla <a href='http://inf3331.no'>felis. Curabitur rhoncus tincidunt varius. Cras</a> gravida metus ut <a href="www.wikipedia.org/wiki/vestibulum">Search Wikipedia for vestibulum</a> vestibulum. *Integer cursus<i> ex* in rutrum volutpat</i>. Nunc scelerisque gravida risus sed ullamcorper. Proin <a href='https://www.malesuada.com'>lorem,</a> massa <img src="https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif" style="width:100px;height:40px";> quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio <i>bibendum.</i>
"""

verify(parse_downmark, [sample_input], [expected_output])



