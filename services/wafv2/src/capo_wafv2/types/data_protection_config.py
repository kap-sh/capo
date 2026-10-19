"""Generated from Smithy shape ``com.amazonaws.wafv2#DataProtectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.data_protections


class DataProtectionConfig(TypedDict, closed=True):
    data_protections: "capo_wafv2.types.data_protections.DataProtections"
    """<p>An array of data protection configurations for specific web request field types. This is defined for each web ACL. WAF applies the specified protection to all web requests that the web ACL inspects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProtectionConfig) -> dict:
    out: dict = {}
    import capo_wafv2.types.data_protections

    out["DataProtections"] = capo_wafv2.types.data_protections.serialize_aws_json_1_1(
        value["data_protections"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataProtectionConfig:
    out: DataProtectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("DataProtections") is not None:
        import capo_wafv2.types.data_protections

        out["data_protections"] = (
            capo_wafv2.types.data_protections.deserialize_aws_json_1_1(
                data["DataProtections"]
            )
        )
    else:
        out["data_protections"] = []
    return out
