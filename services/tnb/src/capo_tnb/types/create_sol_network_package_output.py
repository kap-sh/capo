"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolNetworkPackageOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_arn
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.nsd_onboarding_state
    import capo_tnb.types.nsd_operational_state
    import capo_tnb.types.nsd_usage_state
    import capo_tnb.types.tag_map


class CreateSolNetworkPackageOutput(TypedDict, closed=True):
    id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network package.</p>"""
    arn: "capo_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_onboarding_state: "capo_tnb.types.nsd_onboarding_state.NsdOnboardingState"
    """<p>Onboarding state of the network service descriptor in the network package.</p>"""
    nsd_operational_state: "capo_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Operational state of the network service descriptor in the network package.</p>"""
    nsd_usage_state: "capo_tnb.types.nsd_usage_state.NsdUsageState"
    """<p>Usage state of the network service descriptor in the network package.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSolNetworkPackageOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_tnb.types.nsd_onboarding_state

    out["nsdOnboardingState"] = capo_tnb.types.nsd_onboarding_state.serialize_json(
        value["nsd_onboarding_state"]
    )
    import capo_tnb.types.nsd_operational_state

    out["nsdOperationalState"] = capo_tnb.types.nsd_operational_state.serialize_json(
        value["nsd_operational_state"]
    )
    import capo_tnb.types.nsd_usage_state

    out["nsdUsageState"] = capo_tnb.types.nsd_usage_state.serialize_json(
        value["nsd_usage_state"]
    )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolNetworkPackageOutput:
    out: CreateSolNetworkPackageOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("nsdOnboardingState") is not None:
        import capo_tnb.types.nsd_onboarding_state

        out["nsd_onboarding_state"] = (
            capo_tnb.types.nsd_onboarding_state.deserialize_json(
                data["nsdOnboardingState"]
            )
        )
    else:
        import typing

        out["nsd_onboarding_state"] = typing.cast(
            "capo_tnb.types.nsd_onboarding_state.NsdOnboardingState", ""
        )
    if data.get("nsdOperationalState") is not None:
        import capo_tnb.types.nsd_operational_state

        out["nsd_operational_state"] = (
            capo_tnb.types.nsd_operational_state.deserialize_json(
                data["nsdOperationalState"]
            )
        )
    else:
        import typing

        out["nsd_operational_state"] = typing.cast(
            "capo_tnb.types.nsd_operational_state.NsdOperationalState", ""
        )
    if data.get("nsdUsageState") is not None:
        import capo_tnb.types.nsd_usage_state

        out["nsd_usage_state"] = capo_tnb.types.nsd_usage_state.deserialize_json(
            data["nsdUsageState"]
        )
    else:
        import typing

        out["nsd_usage_state"] = typing.cast(
            "capo_tnb.types.nsd_usage_state.NsdUsageState", ""
        )
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateSolNetworkPackageOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
