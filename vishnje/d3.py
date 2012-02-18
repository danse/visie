import pkg_resources
source = pkg_resources.resource_string(__name__, 'd3.js')
source = '<script type="text/javascript">'+source.decode()+'</script>'
