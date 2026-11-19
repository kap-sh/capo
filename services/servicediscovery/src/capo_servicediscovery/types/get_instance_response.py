"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.instance


class GetInstanceResponse(TypedDict, closed=True):
    resource_owner: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the namespace that contains the service that the instance is associated with. If this isn't your account ID, it's the ID of the account that shared the namespace with your account.</p>"""
    instance: NotRequired["capo_servicediscovery.types.instance.Instance"]
    """<p>A complex type that contains information about a specified instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceResponse) -> dict:
    out: dict = {}
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "instance" in value:
        import capo_servicediscovery.types.instance

        out["Instance"] = capo_servicediscovery.types.instance.serialize_aws_json_1_1(
            value["instance"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceResponse:
    out: GetInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Instance") is not None:
        import capo_servicediscovery.types.instance

        out["instance"] = capo_servicediscovery.types.instance.deserialize_aws_json_1_1(
            data["Instance"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetInstanceResponse) -> dict:
    out: dict = {}
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "instance" in value:
        import capo_servicediscovery.types.instance

        out["Instance"] = capo_servicediscovery.types.instance.serialize_cbor(
            value["instance"]
        )
    return out


def deserialize_cbor(data: dict) -> GetInstanceResponse:
    out: GetInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceOwner") is not None:
        out["resource_owner"] = data["ResourceOwner"]
    if data.get("Instance") is not None:
        import capo_servicediscovery.types.instance

        out["instance"] = capo_servicediscovery.types.instance.deserialize_cbor(
            data["Instance"]
        )
    return out
