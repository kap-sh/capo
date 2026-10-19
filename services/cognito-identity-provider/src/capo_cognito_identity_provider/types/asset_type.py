"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.asset_bytes_type
    import capo_cognito_identity_provider.types.asset_category_type
    import capo_cognito_identity_provider.types.asset_extension_type
    import capo_cognito_identity_provider.types.color_scheme_mode_type
    import capo_cognito_identity_provider.types.resource_id_type


class AssetType(TypedDict, closed=True):
    category: (
        "capo_cognito_identity_provider.types.asset_category_type.AssetCategoryType"
    )
    """<p>The category that the image corresponds to in your managed login configuration. Managed login has asset categories for different types of logos, backgrounds, and icons.</p>"""
    color_mode: "capo_cognito_identity_provider.types.color_scheme_mode_type.ColorSchemeModeType"
    """<p>The display-mode target of the asset: light, dark, or browser-adaptive. For example, Amazon Cognito displays a dark-mode image only when the browser or application is in dark mode, but displays a browser-adaptive file in all contexts.</p>"""
    extension: (
        "capo_cognito_identity_provider.types.asset_extension_type.AssetExtensionType"
    )
    """<p>The file type of the image file.</p>"""
    bytes: NotRequired[
        "capo_cognito_identity_provider.types.asset_bytes_type.AssetBytesType"
    ]
    """<p>The image file, in Base64-encoded binary.</p>"""
    resource_id: NotRequired[
        "capo_cognito_identity_provider.types.resource_id_type.ResourceIdType"
    ]
    """<p>The ID of the asset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.asset_category_type

    out["Category"] = (
        capo_cognito_identity_provider.types.asset_category_type.serialize_aws_json_1_1(
            value["category"]
        )
    )
    import capo_cognito_identity_provider.types.color_scheme_mode_type

    out["ColorMode"] = (
        capo_cognito_identity_provider.types.color_scheme_mode_type.serialize_aws_json_1_1(
            value["color_mode"]
        )
    )
    import capo_cognito_identity_provider.types.asset_extension_type

    out["Extension"] = (
        capo_cognito_identity_provider.types.asset_extension_type.serialize_aws_json_1_1(
            value["extension"]
        )
    )
    if "bytes" in value:
        import capo_cognito_identity_provider.types.asset_bytes_type

        out["Bytes"] = (
            capo_cognito_identity_provider.types.asset_bytes_type.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssetType:
    out: AssetType = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_cognito_identity_provider.types.asset_category_type

        out["category"] = (
            capo_cognito_identity_provider.types.asset_category_type.deserialize_aws_json_1_1(
                data["Category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_cognito_identity_provider.types.asset_category_type.AssetCategoryType",
            "",
        )
    if data.get("ColorMode") is not None:
        import capo_cognito_identity_provider.types.color_scheme_mode_type

        out["color_mode"] = (
            capo_cognito_identity_provider.types.color_scheme_mode_type.deserialize_aws_json_1_1(
                data["ColorMode"]
            )
        )
    else:
        import typing

        out["color_mode"] = typing.cast(
            "capo_cognito_identity_provider.types.color_scheme_mode_type.ColorSchemeModeType",
            "",
        )
    if data.get("Extension") is not None:
        import capo_cognito_identity_provider.types.asset_extension_type

        out["extension"] = (
            capo_cognito_identity_provider.types.asset_extension_type.deserialize_aws_json_1_1(
                data["Extension"]
            )
        )
    else:
        import typing

        out["extension"] = typing.cast(
            "capo_cognito_identity_provider.types.asset_extension_type.AssetExtensionType",
            "",
        )
    if data.get("Bytes") is not None:
        import capo_cognito_identity_provider.types.asset_bytes_type

        out["bytes"] = (
            capo_cognito_identity_provider.types.asset_bytes_type.deserialize_aws_json_1_1(
                data["Bytes"]
            )
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    return out
