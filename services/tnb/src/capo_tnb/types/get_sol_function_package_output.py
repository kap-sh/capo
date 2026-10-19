"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_function_package_metadata
    import capo_tnb.types.onboarding_state
    import capo_tnb.types.operational_state
    import capo_tnb.types.tag_map
    import capo_tnb.types.usage_state
    import capo_tnb.types.vnf_pkg_arn
    import capo_tnb.types.vnf_pkg_id


class GetSolFunctionPackageOutput(TypedDict, closed=True):
    id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>Function package ID.</p>"""
    arn: "capo_tnb.types.vnf_pkg_arn.VnfPkgArn"
    """<p>Function package ARN.</p>"""
    onboarding_state: "capo_tnb.types.onboarding_state.OnboardingState"
    """<p>Function package onboarding state.</p>"""
    operational_state: "capo_tnb.types.operational_state.OperationalState"
    """<p>Function package operational state.</p>"""
    usage_state: "capo_tnb.types.usage_state.UsageState"
    """<p>Function package usage state.</p>"""
    vnfd_id: NotRequired["str"]
    """<p>Function package descriptor ID.</p>"""
    vnf_provider: NotRequired["str"]
    """<p>Network function provider.</p>"""
    vnf_product_name: NotRequired["str"]
    """<p>Network function product name.</p>"""
    vnfd_version: NotRequired["str"]
    """<p>Function package descriptor version.</p>"""
    metadata: NotRequired[
        "capo_tnb.types.get_sol_function_package_metadata.GetSolFunctionPackageMetadata"
    ]
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageOutput) -> dict:
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
    if "vnfd_id" in value:
        out["vnfdId"] = value["vnfd_id"]
    if "vnf_provider" in value:
        out["vnfProvider"] = value["vnf_provider"]
    if "vnf_product_name" in value:
        out["vnfProductName"] = value["vnf_product_name"]
    if "vnfd_version" in value:
        out["vnfdVersion"] = value["vnfd_version"]
    if "metadata" in value:
        import capo_tnb.types.get_sol_function_package_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_function_package_metadata.serialize_json(
                value["metadata"]
            )
        )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageOutput:
    out: GetSolFunctionPackageOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("vnfdId") is not None:
        out["vnfd_id"] = data["vnfdId"]
    if data.get("vnfProvider") is not None:
        out["vnf_provider"] = data["vnfProvider"]
    if data.get("vnfProductName") is not None:
        out["vnf_product_name"] = data["vnfProductName"]
    if data.get("vnfdVersion") is not None:
        out["vnfd_version"] = data["vnfdVersion"]
    if data.get("metadata") is not None:
        import capo_tnb.types.get_sol_function_package_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_function_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetSolFunctionPackageOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
