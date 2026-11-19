"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmContributor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.contributor_attributes
    import capo_cloudwatch.types.contributor_id
    import capo_cloudwatch.types.state_reason
    import capo_cloudwatch.types.timestamp


class AlarmContributor(TypedDict, closed=True):
    contributor_id: NotRequired["capo_cloudwatch.types.contributor_id.ContributorId"]
    """<p>The unique identifier for this alarm contributor.</p>"""
    contributor_attributes: NotRequired[
        "capo_cloudwatch.types.contributor_attributes.ContributorAttributes"
    ]
    """<p>A map of attributes that describe the contributor, such as metric dimensions and other identifying characteristics.</p>"""
    state_reason: NotRequired["capo_cloudwatch.types.state_reason.StateReason"]
    """<p>An explanation for the contributor's current state, providing context about why it is in its current condition.</p>"""
    state_transitioned_timestamp: NotRequired[
        "capo_cloudwatch.types.timestamp.Timestamp"
    ]
    """<p>The timestamp when the contributor last transitioned to its current state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmContributor) -> dict:
    out: dict = {}
    if "contributor_id" in value:
        out["ContributorId"] = value["contributor_id"]
    if "contributor_attributes" in value:
        import capo_cloudwatch.types.contributor_attributes

        out["ContributorAttributes"] = (
            capo_cloudwatch.types.contributor_attributes.serialize_aws_json_1_0(
                value["contributor_attributes"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateTransitionedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
                value["state_transitioned_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AlarmContributor:
    out: AlarmContributor = {}  # type: ignore[typeddict-item]
    if data.get("ContributorId") is not None:
        out["contributor_id"] = data["ContributorId"]
    if data.get("ContributorAttributes") is not None:
        import capo_cloudwatch.types.contributor_attributes

        out["contributor_attributes"] = (
            capo_cloudwatch.types.contributor_attributes.deserialize_aws_json_1_0(
                data["ContributorAttributes"]
            )
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateTransitionedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["StateTransitionedTimestamp"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmContributor, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "contributor_id" in value:
        pairs.append((f"{key_prefix}ContributorId", str(value["contributor_id"])))
    if "contributor_attributes" in value:
        import capo_cloudwatch.types.contributor_attributes

        capo_cloudwatch.types.contributor_attributes.serialize_query(
            value["contributor_attributes"], pairs, f"{key_prefix}ContributorAttributes"
        )
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["state_transitioned_timestamp"],
            pairs,
            f"{key_prefix}StateTransitionedTimestamp",
        )


def deserialize_query(el: Element) -> AlarmContributor:
    out: AlarmContributor = {}  # type: ignore[typeddict-item]
    child_contributor_id = el.find("ContributorId")
    if child_contributor_id is not None:
        out["contributor_id"] = str(child_contributor_id.text or "")
    child_contributor_attributes = el.find("ContributorAttributes")
    if child_contributor_attributes is not None:
        import capo_cloudwatch.types.contributor_attributes

        out["contributor_attributes"] = (
            capo_cloudwatch.types.contributor_attributes.deserialize_query(
                child_contributor_attributes
            )
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_state_transitioned_timestamp = el.find("StateTransitionedTimestamp")
    if child_state_transitioned_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_query(
                child_state_transitioned_timestamp
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmContributor) -> dict:
    out: dict = {}
    if "contributor_id" in value:
        out["ContributorId"] = value["contributor_id"]
    if "contributor_attributes" in value:
        import capo_cloudwatch.types.contributor_attributes

        out["ContributorAttributes"] = (
            capo_cloudwatch.types.contributor_attributes.serialize_cbor(
                value["contributor_attributes"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_transitioned_timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["StateTransitionedTimestamp"] = (
            capo_cloudwatch.types.timestamp.serialize_cbor(
                value["state_transitioned_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AlarmContributor:
    out: AlarmContributor = {}  # type: ignore[typeddict-item]
    if data.get("ContributorId") is not None:
        out["contributor_id"] = data["ContributorId"]
    if data.get("ContributorAttributes") is not None:
        import capo_cloudwatch.types.contributor_attributes

        out["contributor_attributes"] = (
            capo_cloudwatch.types.contributor_attributes.deserialize_cbor(
                data["ContributorAttributes"]
            )
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateTransitionedTimestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["state_transitioned_timestamp"] = (
            capo_cloudwatch.types.timestamp.deserialize_cbor(
                data["StateTransitionedTimestamp"]
            )
        )
    return out
