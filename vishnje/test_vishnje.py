import vishnje
from unittest import TestCase

test_page = '''
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
        <script type="text/javascript">
            window.onload=function(e){window.location='http://localhost:8080/stop';};
        </script>
  </body>
</html>
'''

class Test(TestCase):
    def test(self):
        vishnje.main(test_page)
