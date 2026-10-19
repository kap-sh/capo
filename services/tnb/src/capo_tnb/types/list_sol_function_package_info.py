"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionPackageInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_function_package_metadata
    import capo_tnb.types.onboarding_state
    import capo_tnb.types.operational_state
    import capo_tnb.types.usage_state
    import capo_tnb.types.vnf_pkg_arn
    import capo_tnb.types.vnf_pkg_id


class ListSolFunctionPackageInfo(TypedDict, closed=True):
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
    vnfd_id: NotRequired["str"]
    """<p>Identifies the function package and the function package descriptor.</p>"""
    vnf_provider: NotRequired["str"]
    """<p>Provider of the function package and the function package descriptor.</p>"""
    vnf_product_name: NotRequired["str"]
    """<p>The product name for the network function.</p>"""
    vnfd_version: NotRequired["str"]
    """<p>Identifies the version of the function package descriptor.</p>"""
    metadata: NotRequired[
        "capo_tnb.types.list_sol_function_package_metadata.ListSolFunctionPackageMetadata"
    ]
    """<p>The metadata of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionPackageInfo) -> dict:
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
        import capo_tnb.types.list_sol_function_package_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_function_package_metadata.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSolFunctionPackageInfo:
    out: ListSolFunctionPackageInfo = {}  # type: ignore[typeddict-item]
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
        import capo_tnb.types.list_sol_function_package_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_function_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    return out
