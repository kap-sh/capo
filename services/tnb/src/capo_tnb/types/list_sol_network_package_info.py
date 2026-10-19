"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkPackageInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_network_package_metadata
    import capo_tnb.types.nsd_info_arn
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.nsd_onboarding_state
    import capo_tnb.types.nsd_operational_state
    import capo_tnb.types.nsd_usage_state
    import capo_tnb.types.vnf_pkg_id_list


class ListSolNetworkPackageInfo(TypedDict, closed=True):
    id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the individual network package.</p>"""
    arn: "capo_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_onboarding_state: "capo_tnb.types.nsd_onboarding_state.NsdOnboardingState"
    """<p>Onboarding state of the network service descriptor in the network package.</p>"""
    nsd_operational_state: "capo_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Operational state of the network service descriptor in the network package.</p>"""
    nsd_usage_state: "capo_tnb.types.nsd_usage_state.NsdUsageState"
    """<p>Usage state of the network service descriptor in the network package.</p>"""
    nsd_id: NotRequired["str"]
    """<p>ID of the network service descriptor on which the network package is based.</p>"""
    nsd_name: NotRequired["str"]
    """<p>Name of the onboarded network service descriptor in the network package.</p>"""
    nsd_version: NotRequired["str"]
    """<p>Version of the onboarded network service descriptor in the network package.</p>"""
    nsd_designer: NotRequired["str"]
    """<p>Designer of the onboarded network service descriptor in the network package.</p>"""
    nsd_invariant_id: NotRequired["str"]
    """<p>Identifies a network service descriptor in a version independent manner.</p>"""
    vnf_pkg_ids: NotRequired["capo_tnb.types.vnf_pkg_id_list.VnfPkgIdList"]
    """<p>Identifies the function package for the function package descriptor referenced by the onboarded network package.</p>"""
    metadata: (
        "capo_tnb.types.list_sol_network_package_metadata.ListSolNetworkPackageMetadata"
    )
    """<p>The metadata of the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkPackageInfo) -> dict:
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
    if "nsd_id" in value:
        out["nsdId"] = value["nsd_id"]
    if "nsd_name" in value:
        out["nsdName"] = value["nsd_name"]
    if "nsd_version" in value:
        out["nsdVersion"] = value["nsd_version"]
    if "nsd_designer" in value:
        out["nsdDesigner"] = value["nsd_designer"]
    if "nsd_invariant_id" in value:
        out["nsdInvariantId"] = value["nsd_invariant_id"]
    if "vnf_pkg_ids" in value:
        import capo_tnb.types.vnf_pkg_id_list

        out["vnfPkgIds"] = capo_tnb.types.vnf_pkg_id_list.serialize_json(
            value["vnf_pkg_ids"]
        )
    import capo_tnb.types.list_sol_network_package_metadata

    out["metadata"] = capo_tnb.types.list_sol_network_package_metadata.serialize_json(
        value["metadata"]
    )
    return out


def deserialize_json(data: dict) -> ListSolNetworkPackageInfo:
    out: ListSolNetworkPackageInfo = {}  # type: ignore[typeddict-item]
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
    if data.get("nsdId") is not None:
        out["nsd_id"] = data["nsdId"]
    if data.get("nsdName") is not None:
        out["nsd_name"] = data["nsdName"]
    if data.get("nsdVersion") is not None:
        out["nsd_version"] = data["nsdVersion"]
    if data.get("nsdDesigner") is not None:
        out["nsd_designer"] = data["nsdDesigner"]
    if data.get("nsdInvariantId") is not None:
        out["nsd_invariant_id"] = data["nsdInvariantId"]
    if data.get("vnfPkgIds") is not None:
        import capo_tnb.types.vnf_pkg_id_list

        out["vnf_pkg_ids"] = capo_tnb.types.vnf_pkg_id_list.deserialize_json(
            data["vnfPkgIds"]
        )
    if data.get("metadata") is not None:
        import capo_tnb.types.list_sol_network_package_metadata

        out["metadata"] = (
            capo_tnb.types.list_sol_network_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("ListSolNetworkPackageInfo.metadata required")
    return out
