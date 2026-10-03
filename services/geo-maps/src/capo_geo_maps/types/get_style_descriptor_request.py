"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStyleDescriptorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_maps.types.api_key
    import capo_geo_maps.types.buildings
    import capo_geo_maps.types.color_scheme
    import capo_geo_maps.types.contour_density
    import capo_geo_maps.types.country_code
    import capo_geo_maps.types.map_style
    import capo_geo_maps.types.poi_category_list
    import capo_geo_maps.types.poi_density
    import capo_geo_maps.types.terrain
    import capo_geo_maps.types.traffic
    import capo_geo_maps.types.travel_mode_list


class GetStyleDescriptorRequest(TypedDict, closed=True):
    style: "capo_geo_maps.types.map_style.MapStyle"
    """<p>Style specifies the desired map style. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>Standard</code> and <code>Monochrome</code> values.</p>"""
    color_scheme: NotRequired["capo_geo_maps.types.color_scheme.ColorScheme"]
    """<p>Sets the color tone for the map, such as dark and light.</p> <p>Example: <code>Light</code> </p> <p>Default value: <code>Light</code> </p> <note> <p>Valid values for ColorScheme are case sensitive.</p> </note>"""
    political_view: NotRequired["capo_geo_maps.types.country_code.CountryCode"]
    """<p>Specifies the political view using ISO 3166-2 or ISO 3166-3 country code format. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> <p>The following political views are currently supported:</p> <ul> <li> <p> <code>ARG</code>: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands</p> </li> <li> <p> <code>EGY</code>: Egypt's view on Bir Tawil</p> </li> <li> <p> <code>IND</code>: India's view on Gilgit-Baltistan</p> </li> <li> <p> <code>KEN</code>: Kenya's view on the Ilemi Triangle</p> </li> <li> <p> <code>MAR</code>: Morocco's view on Western Sahara</p> </li> <li> <p> <code>RUS</code>: Russia's view on Crimea</p> </li> <li> <p> <code>SDN</code>: Sudan's view on the Halaib Triangle</p> </li> <li> <p> <code>SRB</code>: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands</p> </li> <li> <p> <code>SUR</code>: Suriname's view on the Courantyne Headwaters and Lawa Headwaters</p> </li> <li> <p> <code>SYR</code>: Syria's view on the Golan Heights</p> </li> <li> <p> <code>TUR</code>: Turkey's view on Cyprus and Northern Cyprus</p> </li> <li> <p> <code>TZA</code>: Tanzania's view on Lake Malawi</p> </li> <li> <p> <code>URY</code>: Uruguay's view on Rincon de Artigas</p> </li> <li> <p> <code>VNM</code>: Vietnam's view on the Paracel Islands and Spratly Islands</p> </li> </ul>"""
    terrain: NotRequired["capo_geo_maps.types.terrain.Terrain"]
    """<p>Adjusts how physical terrain details are rendered on the map. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> <p>The following terrain styles are currently supported:</p> <ul> <li> <p> <code>Hillshade</code>: Displays the physical terrain details through shading and highlighting of elevation change and geographic features.</p> </li> <li> <p> <code>Terrain3D</code>: Displays physical terrain details and elevations as a three-dimensional model.</p> </li> </ul> <p> <code>Hillshade</code> is valid only for the <code>Standard</code> and <code>Monochrome</code> map styles.</p>"""
    contour_density: NotRequired["capo_geo_maps.types.contour_density.ContourDensity"]
    """<p>Displays the shape and steepness of terrain features using elevation lines. The density value controls how densely the available contour line information is rendered on the map. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> <p>This parameter is valid for all map styles except <code>Satellite</code>.</p>"""
    traffic: NotRequired["capo_geo_maps.types.traffic.Traffic"]
    """<p>Displays real-time traffic information overlay on map, such as incident events and flow events. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> <p>This parameter is valid for all map styles except <code>Satellite</code>.</p>"""
    travel_modes: NotRequired["capo_geo_maps.types.travel_mode_list.TravelModeList"]
    """<p>Renders additional map information relevant to selected travel modes. Information for multiple travel modes can be displayed simultaneously, although this increases the overall information density rendered on the map. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> <p>This parameter is valid for all map styles except <code>Satellite</code>.</p>"""
    buildings: NotRequired["capo_geo_maps.types.buildings.Buildings"]
    """<p>Adjusts how building details are rendered on the map.</p> <p>The following building styles are currently supported:</p> <ul> <li> <p> <code>Buildings3D</code>: Displays buildings as three-dimensional extrusions on the map.</p> </li> </ul> <p> <code>Buildings3D</code> is valid only for the <code>Standard</code> and <code>Monochrome</code> map styles.</p>"""
    poi_density: NotRequired["capo_geo_maps.types.poi_density.PoiDensity"]
    """<p>Controls how densely points of interest are rendered on the map. The density value controls the zoom level at which each category of points of interest appears, and how quickly less prominent points of interest are revealed as you zoom in. Denser values display more points of interest at lower zoom levels.</p> <p>Use <code>Off</code> to hide all points of interest. When you omit this parameter, the map renders at <code>Default</code> density.</p> <note> <p>The difference between density values is most noticeable at mid-range zoom levels. At high zoom levels, all density values converge on displaying every available point of interest.</p> </note> <p>This parameter is valid only for the <code>Standard</code> and <code>Hybrid</code> map styles. In <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, this parameter is valid only for the <code>Standard</code> map style.</p>"""
    poi_categories: NotRequired["capo_geo_maps.types.poi_category_list.PoiCategoryList"]
    """<p>Renders only the specified categories of points of interest. When you omit this parameter, the map renders all categories.</p> <p>The following categories are currently supported:</p> <ul> <li> <p> <code>FoodAndDrink</code> </p> </li> <li> <p> <code>Entertainment</code> </p> </li> <li> <p> <code>SightsAndMuseums</code> </p> </li> <li> <p> <code>Transportation</code> </p> </li> <li> <p> <code>Accommodations</code> </p> </li> <li> <p> <code>LeisureAndOutdoor</code> </p> </li> <li> <p> <code>Shopping</code> </p> </li> <li> <p> <code>BusinessAndServices</code> </p> </li> <li> <p> <code>FacilitiesAndBuildings</code> </p> </li> </ul> <p>Specify each category as a separate <code>poi-categories</code> query parameter. Duplicate values are rejected.</p> <note> <p>This parameter has no effect when <code>poi-density</code> is set to <code>Off</code>, which hides all points of interest regardless of category.</p> </note> <p>This parameter is valid only for the <code>Standard</code> and <code>Hybrid</code> map styles. In <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, this parameter is valid only for the <code>Standard</code> map style.</p>"""
    key: NotRequired["capo_geo_maps.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStyleDescriptorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStyleDescriptorRequest:
    out: GetStyleDescriptorRequest = {}  # type: ignore[typeddict-item]
    return out
