"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListAddonInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_instances
    import capo_mailmanager.types.pagination_token


class ListAddonInstancesResponse(TypedDict, closed=True):
    addon_instances: NotRequired[
        "capo_mailmanager.types.addon_instances.AddonInstances"
    ]
    """<p>The list of ingress endpoints.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAddonInstancesResponse) -> dict:
    out: dict = {}
    if "addon_instances" in value:
        import capo_mailmanager.types.addon_instances

        out["AddonInstances"] = (
            capo_mailmanager.types.addon_instances.serialize_aws_json_1_0(
                value["addon_instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAddonInstancesResponse:
    out: ListAddonInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonInstances") is not None:
        import capo_mailmanager.types.addon_instances

        out["addon_instances"] = (
            capo_mailmanager.types.addon_instances.deserialize_aws_json_1_0(
                data["AddonInstances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAddonInstancesResponse) -> dict:
    out: dict = {}
    if "addon_instances" in value:
        import capo_mailmanager.types.addon_instances

        out["AddonInstances"] = capo_mailmanager.types.addon_instances.serialize_cbor(
            value["addon_instances"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAddonInstancesResponse:
    out: ListAddonInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonInstances") is not None:
        import capo_mailmanager.types.addon_instances

        out["addon_instances"] = (
            capo_mailmanager.types.addon_instances.deserialize_cbor(
                data["AddonInstances"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
