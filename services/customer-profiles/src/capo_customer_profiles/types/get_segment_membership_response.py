"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentMembershipResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.failures
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.profiles
    import capo_customer_profiles.types.timestamp


class GetSegmentMembershipResponse(TypedDict, closed=True):
    segment_definition_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The unique name of the segment definition.</p>"""
    profiles: NotRequired["capo_customer_profiles.types.profiles.Profiles"]
    """<p>An array of maps where each contains a response per profile requested.</p>"""
    failures: NotRequired["capo_customer_profiles.types.failures.Failures"]
    """<p>An array of maps where each contains a response per profile failed for the request.</p>"""
    last_computed_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp indicating when the segment membership was last computed or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentMembershipResponse) -> dict:
    out: dict = {}
    if "segment_definition_name" in value:
        out["SegmentDefinitionName"] = value["segment_definition_name"]
    if "profiles" in value:
        import capo_customer_profiles.types.profiles

        out["Profiles"] = capo_customer_profiles.types.profiles.serialize_json(
            value["profiles"]
        )
    if "failures" in value:
        import capo_customer_profiles.types.failures

        out["Failures"] = capo_customer_profiles.types.failures.serialize_json(
            value["failures"]
        )
    if "last_computed_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastComputedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_computed_at"]
        )
    return out


def deserialize_json(data: dict) -> GetSegmentMembershipResponse:
    out: GetSegmentMembershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("SegmentDefinitionName") is not None:
        out["segment_definition_name"] = data["SegmentDefinitionName"]
    if data.get("Profiles") is not None:
        import capo_customer_profiles.types.profiles

        out["profiles"] = capo_customer_profiles.types.profiles.deserialize_json(
            data["Profiles"]
        )
    if data.get("Failures") is not None:
        import capo_customer_profiles.types.failures

        out["failures"] = capo_customer_profiles.types.failures.deserialize_json(
            data["Failures"]
        )
    if data.get("LastComputedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_computed_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastComputedAt"]
            )
        )
    return out


def redact_sensitive(value: GetSegmentMembershipResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "profiles" in value:
        import capo_customer_profiles.types.profiles

        out["profiles"] = capo_customer_profiles.types.profiles.redact_sensitive(
            value["profiles"]
        )
    return out
