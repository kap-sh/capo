"""Generated from Smithy shape ``com.amazonaws.health#DescribeTagKeysForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.organization_tag_key_list


class DescribeTagKeysForOrganizationResponse(TypedDict, closed=True):
    keys: NotRequired[
        "capo_health.types.organization_tag_key_list.OrganizationTagKeyList"
    ]
    """<p>The list of configured tag keys for the organization and their status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagKeysForOrganizationResponse) -> dict:
    out: dict = {}
    if "keys" in value:
        import capo_health.types.organization_tag_key_list

        out["keys"] = (
            capo_health.types.organization_tag_key_list.serialize_aws_json_1_1(
                value["keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagKeysForOrganizationResponse:
    out: DescribeTagKeysForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("keys") is not None:
        import capo_health.types.organization_tag_key_list

        out["keys"] = (
            capo_health.types.organization_tag_key_list.deserialize_aws_json_1_1(
                data["keys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTagKeysForOrganizationResponse) -> dict:
    out: dict = {}
    if "keys" in value:
        import capo_health.types.organization_tag_key_list

        out["keys"] = capo_health.types.organization_tag_key_list.serialize_cbor(
            value["keys"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTagKeysForOrganizationResponse:
    out: DescribeTagKeysForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("keys") is not None:
        import capo_health.types.organization_tag_key_list

        out["keys"] = capo_health.types.organization_tag_key_list.deserialize_cbor(
            data["keys"]
        )
    return out
