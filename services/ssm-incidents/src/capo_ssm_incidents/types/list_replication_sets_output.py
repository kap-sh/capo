"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListReplicationSetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.next_token
    import capo_ssm_incidents.types.replication_set_arn_list


class ListReplicationSetsOutput(TypedDict, closed=True):
    replication_set_arns: (
        "capo_ssm_incidents.types.replication_set_arn_list.ReplicationSetArnList"
    )
    """<p>The Amazon Resource Name (ARN) of the list replication set.</p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicationSetsOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.replication_set_arn_list

    out["replicationSetArns"] = (
        capo_ssm_incidents.types.replication_set_arn_list.serialize_json(
            value["replication_set_arns"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReplicationSetsOutput:
    out: ListReplicationSetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("replicationSetArns") is not None:
        import capo_ssm_incidents.types.replication_set_arn_list

        out["replication_set_arns"] = (
            capo_ssm_incidents.types.replication_set_arn_list.deserialize_json(
                data["replicationSetArns"]
            )
        )
    else:
        out["replication_set_arns"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
