

# The class and its functions are designed to write into an empty .html file
# Each object takes three parameters - center latitude and -longitude and the zoom
# for the height of the map



class GoogleMaps_HeatMap(object):
    

    def __init__(self, center_lat, center_lng, zoom, apikey=''):
        self.center = (float(center_lat), float(center_lng))
        self.zoom = int(zoom)
        self.apikey = str(apikey)
        self.circles = []
        self.heatmap_points = []
    
    # Used to append circles to __init__, so they can be drawn to make the heatmap

    def circle(self, lat, lng, radius):
        self.circles.append(lat, lng, radius)
    

    # Adds heatmap_points to __init__, so they can be drawn by draw_heatmap
    # Parameters threshold and radius are adjusted empirically, giving a reasonably
    # relevant heatmap 

    def heatmap(self, lats, lngs, threshold=50, radius=8, gradient=None, opacity=0.8, maxIntensity=0.9, dissipating=True):
        
        settings_dict = {'threshold': threshold, 'radius': radius, 'gradient': gradient, 'opacity': opacity, 'maxIntensity': maxIntensity, 'dissipating': dissipating}
        settings = ''
        settings += "heatmap.set('threshold', %d);\n" % settings_dict['threshold']
        settings += "heatmap.set('radius', %d);\n" % settings_dict['radius']
        settings += "heatmap.set('maxIntensity', %d);\n" % settings_dict['maxIntensity']
        settings += "heatmap.set('opacity', %f);\n" % settings_dict['opacity']
        dissipation_string = 'true' if settings_dict['dissipating'] else 'false'
        settings += "heatmap.set('dissipating', %s);\n" % (dissipation_string)

        heatmap_points = []
        for lat, lng in zip(lats, lngs):
            heatmap_points.append((lat, lng))
        self.heatmap_points.append((heatmap_points, settings))



    def draw(self, htmlfile):
        # TODO: Get rid of all the extra write lines and make the functions write between the
        # <html> etc. tags.
        
        file = open(htmlfile, 'w')
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />\n')
        file.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>\n')
        file.write('<title>Google Maps - gmplot </title>\n')
        file.write('<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false&key=%s"></script>\n' % self.apikey )
        file.write('<script type="text/javascript">\n')
        file.write('\tfunction initialize() {\n')
        self.write_map(file)

        # Writing all the circles on to the map
        for circle in self.circles:
            self.circle(file, circle[0], circle[1], circle[2])

        self.draw_heatmap(file)
        file.write('\t}\n')
        file.write('</script>\n')
        file.write('</head>\n')
        file.write('<body style="margin:0px; padding:0px;" onload="initialize()">\n')
        file.write('\t<div id="map_canvas" style="width: 100%; height: 100%;"></div>\n')
        file.write('</body>\n')
        file.write('</html>\n')
        file.close()

    # Provides the actual google maps to the .html file

    def write_map(self,  file):
        file.write('\t\tvar centerlatlng = new google.maps.LatLng(%f, %f);\n' %
                (self.center[0], self.center[1]))
        file.write('\t\tvar myOptions = {\n')
        file.write('\t\t\tzoom: %d,\n' % (self.zoom))
        file.write('\t\t\tcenter: centerlatlng,\n')
        file.write('\t\t\tmapTypeId: google.maps.MapTypeId.ROADMAP\n')
        file.write('\t\t};\n')
        file.write('\t\tvar map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
        file.write('\n')

    # Function draws the heatmap points to the .html file

    def draw_heatmap(self, file):
        for heatmap_points, settings in self.heatmap_points:
            file.write('var heatmap_points = [\n')
            for heatmap_lat, heatmap_lng in heatmap_points:
                file.write('new google.maps.LatLng(%f, %f),\n' %
                        (heatmap_lat, heatmap_lng))               
            file.write('];\n')
            file.write('\n')
            file.write('var pointArray = new google.maps.MVCArray(heatmap_points);' + '\n')
            file.write('var heatmap;' + '\n')
            file.write('heatmap = new google.maps.visualization.HeatmapLayer({' + '\n')
            file.write('\n')
            file.write('data: pointArray' + '\n')
            file.write('});' + '\n')
            file.write('heatmap.setMap(map);' + '\n')
            file.write(settings)
