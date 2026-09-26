"""Generated from Smithy shape ``com.amazonaws.geomaps#MapsService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_geo_maps._auth._signers
import capo_geo_maps._auth._sigv4
from capo_geo_maps._auth._identity import Credentials
from capo_geo_maps._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_geo_maps._auth._zapros_handler import AuthMiddleware
from capo_geo_maps._resources.maps_service.provider_resource import ProviderResource
from capo_geo_maps._services._aws_config import aws_config
from capo_geo_maps._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_geo_maps.types.api_key
    import capo_geo_maps.types.buildings
    import capo_geo_maps.types.color_scheme
    import capo_geo_maps.types.compact_overlay
    import capo_geo_maps.types.contour_density
    import capo_geo_maps.types.country_code
    import capo_geo_maps.types.distance_meters
    import capo_geo_maps.types.geo_json_overlay
    import capo_geo_maps.types.get_glyphs_request
    import capo_geo_maps.types.get_glyphs_response
    import capo_geo_maps.types.get_sprites_request
    import capo_geo_maps.types.get_sprites_response
    import capo_geo_maps.types.get_static_map_request
    import capo_geo_maps.types.get_static_map_response
    import capo_geo_maps.types.get_style_descriptor_request
    import capo_geo_maps.types.get_style_descriptor_response
    import capo_geo_maps.types.get_tile_request
    import capo_geo_maps.types.get_tile_response
    import capo_geo_maps.types.label_size
    import capo_geo_maps.types.language_tag
    import capo_geo_maps.types.map_feature_mode
    import capo_geo_maps.types.map_style
    import capo_geo_maps.types.position_list_string
    import capo_geo_maps.types.position_string
    import capo_geo_maps.types.scale_bar_unit
    import capo_geo_maps.types.sensitive_float
    import capo_geo_maps.types.sensitive_integer
    import capo_geo_maps.types.sensitive_string
    import capo_geo_maps.types.static_map_style
    import capo_geo_maps.types.terrain
    import capo_geo_maps.types.tile_additional_feature_list
    import capo_geo_maps.types.tileset
    import capo_geo_maps.types.traffic
    import capo_geo_maps.types.travel_mode_list
    import capo_geo_maps.types.variant


class GeoMapsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class GeoMapsClient:
    """A client for the ``GeoMaps`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = GeoMapsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.provider_resource = ProviderResource(self)

    def operation_options(
        self, config_overrides: Optional[GeoMapsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: GeoMapsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_glyphs(
        self,
        font_stack: str,
        font_unicode_range: str,
        *,
        config_overrides: Optional[GeoMapsClientConfig] = None,
    ) -> "capo_geo_maps.types.get_glyphs_response.GetGlyphsResponse":
        r"""<p> <code>GetGlyphs</code> returns the map's glyphs.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/styling-labels-with-glyphs.html\">Style labels with glyphs</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            font_stack: <p>Name of the <code>FontStack</code> to retrieve. </p> <p>Example: <code>Amazon Ember Bold,Noto Sans Bold</code>.</p> <p>The supported font stacks are as follows:</p> <ul> <li> <p>Amazon Ember Bold</p> </li> <li> <p>Amazon Ember Bold Italic</p> </li> <li> <p>Amazon Ember Bold,Noto Sans Bold</p> </li> <li> <p>Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold</p> </li> <li> <p>Amazon Ember Condensed RC BdItalic</p> </li> <li> <p>Amazon Ember Condensed RC Bold</p> </li> <li> <p>Amazon Ember Condensed RC Bold Italic</p> </li> <li> <p>Amazon Ember Condensed RC Bold,Noto Sans Bold</p> </li> <li> <p>Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold</p> </li> <li> <p>Amazon Ember Condensed RC Light</p> </li> <li> <p>Amazon Ember Condensed RC Light Italic</p> </li> <li> <p>Amazon Ember Condensed RC LtItalic</p> </li> <li> <p>Amazon Ember Condensed RC Regular</p> </li> <li> <p>Amazon Ember Condensed RC Regular Italic</p> </li> <li> <p>Amazon Ember Condensed RC Regular,Noto Sans Regular</p> </li> <li> <p>Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular</p> </li> <li> <p>Amazon Ember Condensed RC RgItalic</p> </li> <li> <p>Amazon Ember Condensed RC ThItalic</p> </li> <li> <p>Amazon Ember Condensed RC Thin</p> </li> <li> <p>Amazon Ember Condensed RC Thin Italic</p> </li> <li> <p>Amazon Ember Heavy</p> </li> <li> <p>Amazon Ember Heavy Italic</p> </li> <li> <p>Amazon Ember Light</p> </li> <li> <p>Amazon Ember Light Italic</p> </li> <li> <p>Amazon Ember Medium</p> </li> <li> <p>Amazon Ember Medium Italic</p> </li> <li> <p>Amazon Ember Medium,Noto Sans Medium</p> </li> <li> <p>Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium</p> </li> <li> <p>Amazon Ember Regular</p> </li> <li> <p>Amazon Ember Regular Italic</p> </li> <li> <p>Amazon Ember Regular Italic,Noto Sans Italic</p> </li> <li> <p>Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular</p> </li> <li> <p>Amazon Ember Regular,Noto Sans Regular</p> </li> <li> <p>Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular</p> </li> <li> <p>Amazon Ember Thin</p> </li> <li> <p>Amazon Ember Thin Italic</p> </li> <li> <p>AmazonEmberCdRC_Bd</p> </li> <li> <p>AmazonEmberCdRC_BdIt</p> </li> <li> <p>AmazonEmberCdRC_Lt</p> </li> <li> <p>AmazonEmberCdRC_LtIt</p> </li> <li> <p>AmazonEmberCdRC_Rg</p> </li> <li> <p>AmazonEmberCdRC_RgIt</p> </li> <li> <p>AmazonEmberCdRC_Th</p> </li> <li> <p>AmazonEmberCdRC_ThIt</p> </li> <li> <p>AmazonEmber_Bd</p> </li> <li> <p>AmazonEmber_BdIt</p> </li> <li> <p>AmazonEmber_He</p> </li> <li> <p>AmazonEmber_HeIt</p> </li> <li> <p>AmazonEmber_Lt</p> </li> <li> <p>AmazonEmber_LtIt</p> </li> <li> <p>AmazonEmber_Md</p> </li> <li> <p>AmazonEmber_MdIt</p> </li> <li> <p>AmazonEmber_Rg</p> </li> <li> <p>AmazonEmber_RgIt</p> </li> <li> <p>AmazonEmber_Th</p> </li> <li> <p>AmazonEmber_ThIt</p> </li> <li> <p>Noto Sans Black</p> </li> <li> <p>Noto Sans Black Italic</p> </li> <li> <p>Noto Sans Bold</p> </li> <li> <p>Noto Sans Bold Italic</p> </li> <li> <p>Noto Sans Extra Bold</p> </li> <li> <p>Noto Sans Extra Bold Italic</p> </li> <li> <p>Noto Sans Extra Light</p> </li> <li> <p>Noto Sans Extra Light Italic</p> </li> <li> <p>Noto Sans Italic</p> </li> <li> <p>Noto Sans Light</p> </li> <li> <p>Noto Sans Light Italic</p> </li> <li> <p>Noto Sans Medium</p> </li> <li> <p>Noto Sans Medium Italic</p> </li> <li> <p>Noto Sans Regular</p> </li> <li> <p>Noto Sans Semi Bold</p> </li> <li> <p>Noto Sans Semi Bold Italic</p> </li> <li> <p>Noto Sans Thin</p> </li> <li> <p>Noto Sans Thin Italic</p> </li> <li> <p>NotoSans-Bold</p> </li> <li> <p>NotoSans-Italic</p> </li> <li> <p>NotoSans-Medium</p> </li> <li> <p>NotoSans-Regular</p> </li> <li> <p>Open Sans Regular,Arial Unicode MS Regular</p> </li> </ul>
            font_unicode_range: <p>A Unicode range of characters to download glyphs for. This must be aligned to multiples of 256. </p> <p>Example: <code>0-255.pbf</code> </p>

        Raises:
            capo_geo_maps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_maps.types.get_glyphs_request.GetGlyphsRequest]",
        ) -> OperationResponse[
            "capo_geo_maps.types.get_glyphs_response.GetGlyphsResponse"
        ]:
            import capo_geo_maps._operations.maps_service.get_glyphs

            output, http_response = (
                capo_geo_maps._operations.maps_service.get_glyphs.get_glyphs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_maps.types.get_glyphs_request.GetGlyphsRequest = {
            "font_stack": font_stack,
            "font_unicode_range": font_unicode_range,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sprites(
        self,
        file_name: str,
        style: "capo_geo_maps.types.map_style.MapStyle",
        color_scheme: "capo_geo_maps.types.color_scheme.ColorScheme",
        variant: "capo_geo_maps.types.variant.Variant",
        *,
        config_overrides: Optional[GeoMapsClientConfig] = None,
    ) -> "capo_geo_maps.types.get_sprites_response.GetSpritesResponse":
        r"""<p> <code>GetSprites</code> returns the map's sprites.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/styling-iconography-with-sprites.html\">Style iconography with sprites</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            file_name: <p> <code>Sprites</code> API: The name of the sprite ﬁle to retrieve, following pattern <code>sprites(@2x)?\.(png|json)</code>.</p> <p>Example: <code>sprites.png</code> </p>
            style: <p>Style specifies the desired map style for the <code>Sprites</code> APIs.</p>
            color_scheme: <p>Sets the color tone for the map sprites, such as dark and light.</p> <p>Example: <code>Light</code> </p> <p>Default value: <code>Light</code> </p> <note> <p>Valid values for ColorScheme are case sensitive.</p> </note>
            variant: <p>Optimizes map styles for specific use case or industry. You can choose allowed variant only with Standard map style.</p> <p>Example: <code>Default</code> </p> <note> <p>Valid values for Variant are case sensitive.</p> </note>

        Raises:
            capo_geo_maps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_maps.types.get_sprites_request.GetSpritesRequest]",
        ) -> OperationResponse[
            "capo_geo_maps.types.get_sprites_response.GetSpritesResponse"
        ]:
            import capo_geo_maps._operations.maps_service.get_sprites

            output, http_response = (
                capo_geo_maps._operations.maps_service.get_sprites.get_sprites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_maps.types.get_sprites_request.GetSpritesRequest = {
            "file_name": file_name,
            "style": style,
            "color_scheme": color_scheme,
            "variant": variant,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_static_map(
        self,
        height: "capo_geo_maps.types.sensitive_integer.SensitiveInteger",
        file_name: str,
        width: "capo_geo_maps.types.sensitive_integer.SensitiveInteger",
        *,
        config_overrides: Optional[GeoMapsClientConfig] = None,
        bounding_box: Optional[
            "capo_geo_maps.types.position_list_string.PositionListString"
        ] = None,
        bounded_positions: Optional[
            "capo_geo_maps.types.position_list_string.PositionListString"
        ] = None,
        center: Optional["capo_geo_maps.types.position_string.PositionString"] = None,
        color_scheme: Optional["capo_geo_maps.types.color_scheme.ColorScheme"] = None,
        compact_overlay: Optional[
            "capo_geo_maps.types.compact_overlay.CompactOverlay"
        ] = None,
        crop_labels: Optional[bool] = None,
        geo_json_overlay: Optional[
            "capo_geo_maps.types.geo_json_overlay.GeoJsonOverlay"
        ] = None,
        key: Optional["capo_geo_maps.types.api_key.ApiKey"] = None,
        label_size: Optional["capo_geo_maps.types.label_size.LabelSize"] = None,
        language: Optional["capo_geo_maps.types.language_tag.LanguageTag"] = None,
        padding: Optional[
            "capo_geo_maps.types.sensitive_integer.SensitiveInteger"
        ] = None,
        political_view: Optional["capo_geo_maps.types.country_code.CountryCode"] = None,
        points_of_interests: Optional[
            "capo_geo_maps.types.map_feature_mode.MapFeatureMode"
        ] = None,
        radius: Optional["capo_geo_maps.types.distance_meters.DistanceMeters"] = None,
        scale_bar_unit: Optional[
            "capo_geo_maps.types.scale_bar_unit.ScaleBarUnit"
        ] = None,
        style: Optional["capo_geo_maps.types.static_map_style.StaticMapStyle"] = None,
        zoom: Optional["capo_geo_maps.types.sensitive_float.SensitiveFloat"] = None,
    ) -> "capo_geo_maps.types.get_static_map_response.GetStaticMapResponse":
        r"""<note> <p>This operation is not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> </note> <p> <code>GetStaticMap</code> provides high-quality static map images with customizable options. You can modify the map's appearance and overlay additional information. It's an ideal solution for applications requiring tailored static map snapshots.</p> <p>For more information, see the following topics in the <i>Amazon Location Service Developer Guide</i>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/static-maps.html\">Static maps</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/customizing-static-maps.html\">Customize static maps</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/overlaying-static-map.html\">Overlay on the static map</a> </p> </li> </ul>

        Args:
            bounding_box: <p>Takes in two pairs of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], denoting south-westerly and north-easterly edges of the image. The underlying area becomes the view of the image. </p> <p>Example: -123.17075,49.26959,-123.08125,49.31429</p>
            bounded_positions: <p>Takes in two or more pair of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], with each coordinate separated by a comma. The API will generate an image to encompass all of the provided coordinates. </p> <note> <p>Cannot be used with <code>Zoom</code> and or <code>Radius</code> </p> </note> <p>Example: 97.170451,78.039098,99.045536,27.176178</p>
            center: <p>Takes in a pair of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], which becomes the center point of the image. This parameter requires that either zoom or radius is set.</p> <note> <p>Cannot be used with <code>Zoom</code> and or <code>Radius</code> </p> </note> <p>Example: 49.295,-123.108</p>
            color_scheme: <p>Sets the color tone for the map, such as dark and light.</p> <p>Example: <code>Light</code> </p> <p>Default value: <code>Light</code> </p> <note> <p>Valid values for <code>ColorScheme</code> are case sensitive.</p> </note>
            compact_overlay: <p>Takes in a string to draw geometries on the image. The input is a comma separated format as follows format: <code>[Lon, Lat]</code> </p> <p>Example: <code>line:-122.407653,37.798557,-122.413291,37.802443;color=%23DD0000;width=7;outline-color=#00DD00;outline-width=5yd|point:-122.40572,37.80004;label=Fog Hill Market;size=large;text-color=%23DD0000;color=#EE4B2B</code> </p> <note> <p>Currently it supports the following geometry types: point, line and polygon. It does not support multiPoint , multiLine and multiPolgyon.</p> </note>
            crop_labels: <p>It is a flag that takes in true or false. It prevents the labels that are on the edge of the image from being cut or obscured.</p>
            geo_json_overlay: <p>Takes in a string to draw geometries on the image. The input is a valid GeoJSON collection object. </p> <p>Example: <code>{\"type\":\"FeatureCollection\",\"features\": [{\"type\":\"Feature\",\"geometry\":{\"type\":\"MultiPoint\",\"coordinates\": [[-90.076345,51.504107],[-0.074451,51.506892]]},\"properties\": {\"color\":\"#00DD00\"}}]}</code> </p>
            height: <p>Specifies the height of the map image.</p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>
            label_size: <p>Overrides the label size auto-calculated by <code>FileName</code>. Takes in one of the values - <code>Small</code> or <code>Large</code>.</p>
            language: <p>Specifies the language on the map labels using the BCP 47 language tag, limited to ISO 639-1 two-letter language codes. If the specified language data isn't available for the map image, the labels will default to the regional primary language.</p> <p>Supported codes:</p> <ul> <li> <p> <code>ar</code> </p> </li> <li> <p> <code>as</code> </p> </li> <li> <p> <code>az</code> </p> </li> <li> <p> <code>be</code> </p> </li> <li> <p> <code>bg</code> </p> </li> <li> <p> <code>bn</code> </p> </li> <li> <p> <code>bs</code> </p> </li> <li> <p> <code>ca</code> </p> </li> <li> <p> <code>cs</code> </p> </li> <li> <p> <code>cy</code> </p> </li> <li> <p> <code>da</code> </p> </li> <li> <p> <code>de</code> </p> </li> <li> <p> <code>el</code> </p> </li> <li> <p> <code>en</code> </p> </li> <li> <p> <code>es</code> </p> </li> <li> <p> <code>et</code> </p> </li> <li> <p> <code>eu</code> </p> </li> <li> <p> <code>fi</code> </p> </li> <li> <p> <code>fo</code> </p> </li> <li> <p> <code>fr</code> </p> </li> <li> <p> <code>ga</code> </p> </li> <li> <p> <code>gl</code> </p> </li> <li> <p> <code>gn</code> </p> </li> <li> <p> <code>gu</code> </p> </li> <li> <p> <code>he</code> </p> </li> <li> <p> <code>hi</code> </p> </li> <li> <p> <code>hr</code> </p> </li> <li> <p> <code>hu</code> </p> </li> <li> <p> <code>hy</code> </p> </li> <li> <p> <code>id</code> </p> </li> <li> <p> <code>is</code> </p> </li> <li> <p> <code>it</code> </p> </li> <li> <p> <code>ja</code> </p> </li> <li> <p> <code>ka</code> </p> </li> <li> <p> <code>kk</code> </p> </li> <li> <p> <code>km</code> </p> </li> <li> <p> <code>kn</code> </p> </li> <li> <p> <code>ko</code> </p> </li> <li> <p> <code>ky</code> </p> </li> <li> <p> <code>lt</code> </p> </li> <li> <p> <code>lv</code> </p> </li> <li> <p> <code>mk</code> </p> </li> <li> <p> <code>ml</code> </p> </li> <li> <p> <code>mr</code> </p> </li> <li> <p> <code>ms</code> </p> </li> <li> <p> <code>mt</code> </p> </li> <li> <p> <code>my</code> </p> </li> <li> <p> <code>nl</code> </p> </li> <li> <p> <code>no</code> </p> </li> <li> <p> <code>or</code> </p> </li> <li> <p> <code>pa</code> </p> </li> <li> <p> <code>pl</code> </p> </li> <li> <p> <code>pt</code> </p> </li> <li> <p> <code>ro</code> </p> </li> <li> <p> <code>ru</code> </p> </li> <li> <p> <code>sk</code> </p> </li> <li> <p> <code>sl</code> </p> </li> <li> <p> <code>sq</code> </p> </li> <li> <p> <code>sr</code> </p> </li> <li> <p> <code>sv</code> </p> </li> <li> <p> <code>ta</code> </p> </li> <li> <p> <code>te</code> </p> </li> <li> <p> <code>th</code> </p> </li> <li> <p> <code>tr</code> </p> </li> <li> <p> <code>uk</code> </p> </li> <li> <p> <code>uz</code> </p> </li> <li> <p> <code>vi</code> </p> </li> <li> <p> <code>zh</code> </p> </li> </ul>
            padding: <p>Applies additional space (in pixels) around overlay feature to prevent them from being cut or obscured.</p> <note> <p>Value for max and min is determined by:</p> <p>Min: <code>1</code> </p> <p>Max: <code>min(height, width)/4</code> </p> </note> <p>Example: <code>100</code> </p>
            political_view: <p>Specifies the political view, using ISO 3166-2 or ISO 3166-3 country code format.</p> <p>The following political views are currently supported:</p> <ul> <li> <p> <code>ARG</code>: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands</p> </li> <li> <p> <code>EGY</code>: Egypt's view on Bir Tawil</p> </li> <li> <p> <code>IND</code>: India's view on Gilgit-Baltistan</p> </li> <li> <p> <code>KEN</code>: Kenya's view on the Ilemi Triangle</p> </li> <li> <p> <code>MAR</code>: Morocco's view on Western Sahara</p> </li> <li> <p> <code>RUS</code>: Russia's view on Crimea</p> </li> <li> <p> <code>SDN</code>: Sudan's view on the Halaib Triangle</p> </li> <li> <p> <code>SRB</code>: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands</p> </li> <li> <p> <code>SUR</code>: Suriname's view on the Courantyne Headwaters and Lawa Headwaters</p> </li> <li> <p> <code>SYR</code>: Syria's view on the Golan Heights</p> </li> <li> <p> <code>TUR</code>: Turkey's view on Cyprus and Northern Cyprus</p> </li> <li> <p> <code>TZA</code>: Tanzania's view on Lake Malawi</p> </li> <li> <p> <code>URY</code>: Uruguay's view on Rincon de Artigas</p> </li> <li> <p> <code>VNM</code>: Vietnam's view on the Paracel Islands and Spratly Islands</p> </li> </ul>
            points_of_interests: <p>Determines if the result image will display icons representing points of interest on the map.</p>
            radius: <p>Used with center parameter, it specifies the zoom of the image where you can control it on a granular level. Takes in any value <code>&gt;= 1</code>. </p> <p>Example: <code>1500</code> </p> <note> <p>Cannot be used with <code>Zoom</code>.</p> </note> <p> <b>Unit</b>: <code>Meters</code> </p> <p/>
            file_name: <p>The map scaling parameter to size the image, icons, and labels. It follows the pattern of <code>^map(@2x)?$</code>.</p> <p>Example: <code>map, map@2x</code> </p>
            scale_bar_unit: <p>Displays a scale on the bottom right of the map image with the unit specified in the input. </p> <p>Example: <code>KilometersMiles, Miles, Kilometers, MilesKilometers</code> </p>
            style: <p> <code>Style</code> specifies the desired map style.</p>
            width: <p>Specifies the width of the map image.</p>
            zoom: <p>Specifies the zoom level of the map image.</p> <note> <p>Cannot be used with <code>Radius</code>.</p> </note>

        Raises:
            capo_geo_maps.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_geo_maps.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_maps.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_maps.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_maps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_maps.types.get_static_map_request.GetStaticMapRequest]",
        ) -> OperationResponse[
            "capo_geo_maps.types.get_static_map_response.GetStaticMapResponse"
        ]:
            import capo_geo_maps._operations.maps_service.get_static_map

            output, http_response = (
                capo_geo_maps._operations.maps_service.get_static_map.get_static_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_maps.types.get_static_map_request.GetStaticMapRequest = {
            "height": height,
            "file_name": file_name,
            "width": width,
        }
        if bounding_box is not None:
            input_["bounding_box"] = bounding_box
        if bounded_positions is not None:
            input_["bounded_positions"] = bounded_positions
        if center is not None:
            input_["center"] = center
        if color_scheme is not None:
            input_["color_scheme"] = color_scheme
        if compact_overlay is not None:
            input_["compact_overlay"] = compact_overlay
        if crop_labels is not None:
            input_["crop_labels"] = crop_labels
        if geo_json_overlay is not None:
            input_["geo_json_overlay"] = geo_json_overlay
        if key is not None:
            input_["key"] = key
        if label_size is not None:
            input_["label_size"] = label_size
        if language is not None:
            input_["language"] = language
        if padding is not None:
            input_["padding"] = padding
        if political_view is not None:
            input_["political_view"] = political_view
        if points_of_interests is not None:
            input_["points_of_interests"] = points_of_interests
        if radius is not None:
            input_["radius"] = radius
        if scale_bar_unit is not None:
            input_["scale_bar_unit"] = scale_bar_unit
        if style is not None:
            input_["style"] = style
        if zoom is not None:
            input_["zoom"] = zoom

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_style_descriptor(
        self,
        style: "capo_geo_maps.types.map_style.MapStyle",
        *,
        config_overrides: Optional[GeoMapsClientConfig] = None,
        color_scheme: Optional["capo_geo_maps.types.color_scheme.ColorScheme"] = None,
        political_view: Optional["capo_geo_maps.types.country_code.CountryCode"] = None,
        terrain: Optional["capo_geo_maps.types.terrain.Terrain"] = None,
        contour_density: Optional[
            "capo_geo_maps.types.contour_density.ContourDensity"
        ] = None,
        traffic: Optional["capo_geo_maps.types.traffic.Traffic"] = None,
        travel_modes: Optional[
            "capo_geo_maps.types.travel_mode_list.TravelModeList"
        ] = None,
        buildings: Optional["capo_geo_maps.types.buildings.Buildings"] = None,
        key: Optional["capo_geo_maps.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_maps.types.get_style_descriptor_response.GetStyleDescriptorResponse":
        r"""<p> <code>GetStyleDescriptor</code> returns information about the style.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/styling-dynamic-maps.html\">Style dynamic maps</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            style: <p>Style specifies the desired map style. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>Standard</code> and <code>Monochrome</code> values.</p>
            color_scheme: <p>Sets the color tone for the map, such as dark and light.</p> <p>Example: <code>Light</code> </p> <p>Default value: <code>Light</code> </p> <note> <p>Valid values for ColorScheme are case sensitive.</p> </note>
            political_view: <p>Specifies the political view using ISO 3166-2 or ISO 3166-3 country code format. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <p>The following political views are currently supported:</p> <ul> <li> <p> <code>ARG</code>: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands</p> </li> <li> <p> <code>EGY</code>: Egypt's view on Bir Tawil</p> </li> <li> <p> <code>IND</code>: India's view on Gilgit-Baltistan</p> </li> <li> <p> <code>KEN</code>: Kenya's view on the Ilemi Triangle</p> </li> <li> <p> <code>MAR</code>: Morocco's view on Western Sahara</p> </li> <li> <p> <code>RUS</code>: Russia's view on Crimea</p> </li> <li> <p> <code>SDN</code>: Sudan's view on the Halaib Triangle</p> </li> <li> <p> <code>SRB</code>: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands</p> </li> <li> <p> <code>SUR</code>: Suriname's view on the Courantyne Headwaters and Lawa Headwaters</p> </li> <li> <p> <code>SYR</code>: Syria's view on the Golan Heights</p> </li> <li> <p> <code>TUR</code>: Turkey's view on Cyprus and Northern Cyprus</p> </li> <li> <p> <code>TZA</code>: Tanzania's view on Lake Malawi</p> </li> <li> <p> <code>URY</code>: Uruguay's view on Rincon de Artigas</p> </li> <li> <p> <code>VNM</code>: Vietnam's view on the Paracel Islands and Spratly Islands</p> </li> </ul>
            terrain: <p>Adjusts how physical terrain details are rendered on the map. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <p>The following terrain styles are currently supported:</p> <ul> <li> <p> <code>Hillshade</code>: Displays the physical terrain details through shading and highlighting of elevation change and geographic features.</p> </li> <li> <p> <code>Terrain3D</code>: Displays physical terrain details and elevations as a three-dimensional model.</p> </li> </ul> <p> <code>Hillshade</code> is valid only for the <code>Standard</code> and <code>Monochrome</code> map styles.</p>
            contour_density: <p>Displays the shape and steepness of terrain features using elevation lines. The density value controls how densely the available contour line information is rendered on the map. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <p>This parameter is valid for all map styles except <code>Satellite</code>.</p>
            traffic: <p>Displays real-time traffic information overlay on map, such as incident events and flow events. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <p>This parameter is valid for all map styles except <code>Satellite</code>.</p>
            travel_modes: <p>Renders additional map information relevant to selected travel modes. Information for multiple travel modes can be displayed simultaneously, although this increases the overall information density rendered on the map. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <p>This parameter is valid for all map styles except <code>Satellite</code>.</p>
            buildings: <p>Adjusts how building details are rendered on the map.</p> <p>The following building styles are currently supported:</p> <ul> <li> <p> <code>Buildings3D</code>: Displays buildings as three-dimensional extrusions on the map.</p> </li> </ul> <p> <code>Buildings3D</code> is valid only for the <code>Standard</code> and <code>Monochrome</code> map styles.</p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>

        Raises:
            capo_geo_maps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_maps.types.get_style_descriptor_request.GetStyleDescriptorRequest]",
        ) -> OperationResponse[
            "capo_geo_maps.types.get_style_descriptor_response.GetStyleDescriptorResponse"
        ]:
            import capo_geo_maps._operations.maps_service.get_style_descriptor

            output, http_response = (
                capo_geo_maps._operations.maps_service.get_style_descriptor.get_style_descriptor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_maps.types.get_style_descriptor_request.GetStyleDescriptorRequest = {
            "style": style
        }
        if color_scheme is not None:
            input_["color_scheme"] = color_scheme
        if political_view is not None:
            input_["political_view"] = political_view
        if terrain is not None:
            input_["terrain"] = terrain
        if contour_density is not None:
            input_["contour_density"] = contour_density
        if traffic is not None:
            input_["traffic"] = traffic
        if travel_modes is not None:
            input_["travel_modes"] = travel_modes
        if buildings is not None:
            input_["buildings"] = buildings
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_tile(
        self,
        tileset: "capo_geo_maps.types.tileset.Tileset",
        z: "capo_geo_maps.types.sensitive_string.SensitiveString",
        x: "capo_geo_maps.types.sensitive_string.SensitiveString",
        y: "capo_geo_maps.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[GeoMapsClientConfig] = None,
        additional_features: Optional[
            "capo_geo_maps.types.tile_additional_feature_list.TileAdditionalFeatureList"
        ] = None,
        key: Optional["capo_geo_maps.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_maps.types.get_tile_response.GetTileResponse":
        r"""<p> <code>GetTile</code> returns a tile. Map tiles are used by clients to render a map. They're addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/tiles.html\">Tiles</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            additional_features: <p>A list of optional additional parameters such as map styles that can be requested for each result. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p>
            tileset: <p>Specifies the desired tile set. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>vector.basemap</code> value.</p> <p>Valid Values: <code>raster.satellite | vector.basemap | vector.traffic | raster.dem</code> </p>
            z: <p>The zoom value for the map tile.</p>
            x: <p>The X axis value for the map tile.</p>
            y: <p>The Y axis value for the map tile.</p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>

        Raises:
            capo_geo_maps.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_geo_maps.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_maps.errors.resource_not_found_exception.ResourceNotFoundException: <p>Exception thrown when the associated resource could not be found.</p>
            capo_geo_maps.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_maps.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_maps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_maps.types.get_tile_request.GetTileRequest]",
        ) -> OperationResponse["capo_geo_maps.types.get_tile_response.GetTileResponse"]:
            import capo_geo_maps._operations.maps_service.get_tile

            output, http_response = (
                capo_geo_maps._operations.maps_service.get_tile.get_tile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_maps.types.get_tile_request.GetTileRequest = {
            "tileset": tileset,
            "z": z,
            "x": x,
            "y": y,
        }
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
