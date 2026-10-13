"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileQueryResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile
    import capo_customer_profiles.types.profile_id
    import capo_customer_profiles.types.query_result


class ProfileQueryResult(TypedDict, closed=True):
    profile_id: "capo_customer_profiles.types.profile_id.ProfileId"
    """<p>The profile id the result belongs to.</p>"""
    query_result: "capo_customer_profiles.types.query_result.QueryResult"
    """<p>Describes whether the profile was absent or present in the segment.</p>"""
    profile: NotRequired["capo_customer_profiles.types.profile.Profile"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQueryResult) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_customer_profiles.types.query_result

    out["QueryResult"] = capo_customer_profiles.types.query_result.serialize_json(
        value["query_result"]
    )
    if "profile" in value:
        import capo_customer_profiles.types.profile

        out["Profile"] = capo_customer_profiles.types.profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> ProfileQueryResult:
    out: ProfileQueryResult = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("ProfileQueryResult.profile_id required")
    if data.get("QueryResult") is not None:
        import capo_customer_profiles.types.query_result

        out["query_result"] = (
            capo_customer_profiles.types.query_result.deserialize_json(
                data["QueryResult"]
            )
        )
    else:
        raise DeserializationError("ProfileQueryResult.query_result required")
    if data.get("Profile") is not None:
        import capo_customer_profiles.types.profile

        out["profile"] = capo_customer_profiles.types.profile.deserialize_json(
            data["Profile"]
        )
    return out


def redact_sensitive(value: ProfileQueryResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "profile" in value:
        import capo_customer_profiles.types.profile

        out["profile"] = capo_customer_profiles.types.profile.redact_sensitive(
            value["profile"]
        )
    return out
