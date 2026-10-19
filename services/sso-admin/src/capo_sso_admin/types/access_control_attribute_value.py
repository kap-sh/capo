"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessControlAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.access_control_attribute_value_source_list


class AccessControlAttributeValue(TypedDict, closed=True):
    source: "capo_sso_admin.types.access_control_attribute_value_source_list.AccessControlAttributeValueSourceList"
    """<p>The identity source to use when mapping a specified attribute to IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlAttributeValue) -> dict:
    out: dict = {}
    import capo_sso_admin.types.access_control_attribute_value_source_list

    out["Source"] = (
        capo_sso_admin.types.access_control_attribute_value_source_list.serialize_aws_json_1_1(
            value["source"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessControlAttributeValue:
    out: AccessControlAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        import capo_sso_admin.types.access_control_attribute_value_source_list

        out["source"] = (
            capo_sso_admin.types.access_control_attribute_value_source_list.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    else:
        out["source"] = []
    return out
