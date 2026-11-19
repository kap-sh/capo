"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListHypervisorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.hypervisors
    import capo_backup_gateway.types.next_token


class ListHypervisorsOutput(TypedDict, closed=True):
    hypervisors: NotRequired["capo_backup_gateway.types.hypervisors.Hypervisors"]
    """<p>A list of your <code>Hypervisor</code> objects, ordered by their Amazon Resource Names (ARNs).</p>"""
    next_token: NotRequired["capo_backup_gateway.types.next_token.NextToken"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListHypervisorsOutput) -> dict:
    out: dict = {}
    if "hypervisors" in value:
        import capo_backup_gateway.types.hypervisors

        out["Hypervisors"] = (
            capo_backup_gateway.types.hypervisors.serialize_aws_json_1_0(
                value["hypervisors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListHypervisorsOutput:
    out: ListHypervisorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Hypervisors") is not None:
        import capo_backup_gateway.types.hypervisors

        out["hypervisors"] = (
            capo_backup_gateway.types.hypervisors.deserialize_aws_json_1_0(
                data["Hypervisors"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListHypervisorsOutput) -> dict:
    out: dict = {}
    if "hypervisors" in value:
        import capo_backup_gateway.types.hypervisors

        out["Hypervisors"] = capo_backup_gateway.types.hypervisors.serialize_cbor(
            value["hypervisors"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListHypervisorsOutput:
    out: ListHypervisorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Hypervisors") is not None:
        import capo_backup_gateway.types.hypervisors

        out["hypervisors"] = capo_backup_gateway.types.hypervisors.deserialize_cbor(
            data["Hypervisors"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
