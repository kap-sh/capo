"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.replication_rule_list


class ReplicationConfiguration(TypedDict, closed=True):
    rules: "capo_ecr.types.replication_rule_list.ReplicationRuleList"
    """<p>An array of objects representing the replication destinations and repository filters for a replication configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationConfiguration) -> dict:
    out: dict = {}
    import capo_ecr.types.replication_rule_list

    out["rules"] = capo_ecr.types.replication_rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationConfiguration:
    out: ReplicationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("rules") is not None:
        import capo_ecr.types.replication_rule_list

        out["rules"] = capo_ecr.types.replication_rule_list.deserialize_aws_json_1_1(
            data["rules"]
        )
    else:
        out["rules"] = []
    return out
