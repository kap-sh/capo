"""Generated from Smithy shape ``com.amazonaws.amp#RuleGroupsNamespaceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_amp.types.rule_groups_namespace_arn
    import capo_amp.types.rule_groups_namespace_data
    import capo_amp.types.rule_groups_namespace_name
    import capo_amp.types.rule_groups_namespace_status
    import capo_amp.types.tag_map


class RuleGroupsNamespaceDescription(TypedDict, closed=True):
    arn: "capo_amp.types.rule_groups_namespace_arn.RuleGroupsNamespaceArn"
    """<p>The ARN of the rule groups namespace. For example, <code>arn:aws:aps:&lt;region&gt;:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1</code>.</p>"""
    name: "capo_amp.types.rule_groups_namespace_name.RuleGroupsNamespaceName"
    """<p>The name of the rule groups namespace.</p>"""
    status: "capo_amp.types.rule_groups_namespace_status.RuleGroupsNamespaceStatus"
    """<p>The current status of the rule groups namespace.</p>"""
    data: "capo_amp.types.rule_groups_namespace_data.RuleGroupsNamespaceData"
    """<p>The rule groups file used in the namespace.</p> <p>For details about the rule groups namespace structure, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-RuleGroupsNamespaceData.html">RuleGroupsNamespaceData</a>.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the rule groups namespace was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time that the rule groups namespace was most recently changed.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the rule groups namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupsNamespaceDescription) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_amp.types.rule_groups_namespace_status

    out["status"] = capo_amp.types.rule_groups_namespace_status.serialize_json(
        value["status"]
    )
    import capo_amp.types.rule_groups_namespace_data

    out["data"] = capo_amp.types.rule_groups_namespace_data.serialize_json(
        value["data"]
    )
    import capo_amp.types._prelude.timestamp

    out["createdAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_amp.types._prelude.timestamp

    out["modifiedAt"] = capo_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RuleGroupsNamespaceDescription:
    out: RuleGroupsNamespaceDescription = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RuleGroupsNamespaceDescription.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RuleGroupsNamespaceDescription.name required")
    if data.get("status") is not None:
        import capo_amp.types.rule_groups_namespace_status

        out["status"] = capo_amp.types.rule_groups_namespace_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("RuleGroupsNamespaceDescription.status required")
    if data.get("data") is not None:
        import capo_amp.types.rule_groups_namespace_data

        out["data"] = capo_amp.types.rule_groups_namespace_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("RuleGroupsNamespaceDescription.data required")
    if data.get("createdAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["created_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("RuleGroupsNamespaceDescription.created_at required")
    if data.get("modifiedAt") is not None:
        import capo_amp.types._prelude.timestamp

        out["modified_at"] = capo_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError(
            "RuleGroupsNamespaceDescription.modified_at required"
        )
    if data.get("tags") is not None:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    return out
