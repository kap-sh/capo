"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.rule_set_name


class RuleSet(TypedDict, closed=True):
    rule_set_id: NotRequired["capo_mailmanager.types.rule_set_id.RuleSetId"]
    """<p>The identifier of the rule set.</p>"""
    rule_set_name: NotRequired["capo_mailmanager.types.rule_set_name.RuleSetName"]
    """<p>A user-friendly name for the rule set.</p>"""
    last_modification_date: NotRequired["datetime.datetime"]
    """<p>The last modification date of the rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleSet) -> dict:
    out: dict = {}
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "last_modification_date" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastModificationDate"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_modification_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleSet:
    out: RuleSet = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("LastModificationDate") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_modification_date"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModificationDate"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleSet) -> dict:
    out: dict = {}
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "last_modification_date" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastModificationDate"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_cbor(
                value["last_modification_date"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RuleSet:
    out: RuleSet = {}  # type: ignore[typeddict-item]
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    if data.get("RuleSetName") is not None:
        out["rule_set_name"] = data["RuleSetName"]
    if data.get("LastModificationDate") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_modification_date"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_cbor(
                data["LastModificationDate"]
            )
        )
    return out
