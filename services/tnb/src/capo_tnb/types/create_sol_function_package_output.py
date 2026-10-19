"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolFunctionPackageOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.onboarding_state
    import capo_tnb.types.operational_state
    import capo_tnb.types.tag_map
    import capo_tnb.types.usage_state
    import capo_tnb.types.vnf_pkg_arn
    import capo_tnb.types.vnf_pkg_id


class CreateSolFunctionPackageOutput(TypedDict, closed=True):
    id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""
    arn: "capo_tnb.types.vnf_pkg_arn.VnfPkgArn"
    """<p>Function package ARN.</p>"""
    onboarding_state: "capo_tnb.types.onboarding_state.OnboardingState"
    """<p>Onboarding state of the function package.</p>"""
    operational_state: "capo_tnb.types.operational_state.OperationalState"
    """<p>Operational state of the function package.</p>"""
    usage_state: "capo_tnb.types.usage_state.UsageState"
    """<p>Usage state of the function package.</p>"""
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSolFunctionPackageOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import capo_tnb.types.onboarding_state

    out["onboardingState"] = capo_tnb.types.onboarding_state.serialize_json(
        value["onboarding_state"]
    )
    import capo_tnb.types.operational_state

    out["operationalState"] = capo_tnb.types.operational_state.serialize_json(
        value["operational_state"]
    )
    import capo_tnb.types.usage_state

    out["usageState"] = capo_tnb.types.usage_state.serialize_json(value["usage_state"])
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolFunctionPackageOutput:
    out: CreateSolFunctionPackageOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("onboardingState") is not None:
        import capo_tnb.types.onboarding_state

        out["onboarding_state"] = capo_tnb.types.onboarding_state.deserialize_json(
            data["onboardingState"]
        )
    else:
        import typing

        out["onboarding_state"] = typing.cast(
            "capo_tnb.types.onboarding_state.OnboardingState", ""
        )
    if data.get("operationalState") is not None:
        import capo_tnb.types.operational_state

        out["operational_state"] = capo_tnb.types.operational_state.deserialize_json(
            data["operationalState"]
        )
    else:
        import typing

        out["operational_state"] = typing.cast(
            "capo_tnb.types.operational_state.OperationalState", ""
        )
    if data.get("usageState") is not None:
        import capo_tnb.types.usage_state

        out["usage_state"] = capo_tnb.types.usage_state.deserialize_json(
            data["usageState"]
        )
    else:
        import typing

        out["usage_state"] = typing.cast("capo_tnb.types.usage_state.UsageState", "")
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateSolFunctionPackageOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
