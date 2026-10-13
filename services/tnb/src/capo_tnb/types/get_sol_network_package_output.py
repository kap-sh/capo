"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_network_package_metadata
    import capo_tnb.types.nsd_id
    import capo_tnb.types.nsd_info_arn
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.nsd_onboarding_state
    import capo_tnb.types.nsd_operational_state
    import capo_tnb.types.nsd_usage_state
    import capo_tnb.types.tag_map
    import capo_tnb.types.vnf_pkg_id_list


class GetSolNetworkPackageOutput(TypedDict, closed=True):
    id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network package ID.</p>"""
    arn: "capo_tnb.types.nsd_info_arn.NsdInfoArn"
    """<p>Network package ARN.</p>"""
    nsd_onboarding_state: "capo_tnb.types.nsd_onboarding_state.NsdOnboardingState"
    """<p>Network service descriptor onboarding state.</p>"""
    nsd_operational_state: "capo_tnb.types.nsd_operational_state.NsdOperationalState"
    """<p>Network service descriptor operational state.</p>"""
    nsd_usage_state: "capo_tnb.types.nsd_usage_state.NsdUsageState"
    """<p>Network service descriptor usage state.</p>"""
    nsd_id: "capo_tnb.types.nsd_id.NsdId"
    """<p>Network service descriptor ID.</p>"""
    nsd_name: "str"
    """<p>Network service descriptor name.</p>"""
    nsd_version: "str"
    """<p>Network service descriptor version.</p>"""
    vnf_pkg_ids: "capo_tnb.types.vnf_pkg_id_list.VnfPkgIdList"
    """<p>Identifies the function package for the function package descriptor referenced by the onboarded network package.</p>"""
    metadata: (
        "capo_tnb.types.get_sol_network_package_metadata.GetSolNetworkPackageMetadata"
    )
    tags: NotRequired["capo_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageOutput) -> dict:
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
    out["nsdId"] = value["nsd_id"]
    out["nsdName"] = value["nsd_name"]
    out["nsdVersion"] = value["nsd_version"]
    import capo_tnb.types.vnf_pkg_id_list

    out["vnfPkgIds"] = capo_tnb.types.vnf_pkg_id_list.serialize_json(
        value["vnf_pkg_ids"]
    )
    import capo_tnb.types.get_sol_network_package_metadata

    out["metadata"] = capo_tnb.types.get_sol_network_package_metadata.serialize_json(
        value["metadata"]
    )
    if "tags" in value:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageOutput:
    out: GetSolNetworkPackageOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.arn required")
    if data.get("nsdOnboardingState") is not None:
        import capo_tnb.types.nsd_onboarding_state

        out["nsd_onboarding_state"] = (
            capo_tnb.types.nsd_onboarding_state.deserialize_json(
                data["nsdOnboardingState"]
            )
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageOutput.nsd_onboarding_state required"
        )
    if data.get("nsdOperationalState") is not None:
        import capo_tnb.types.nsd_operational_state

        out["nsd_operational_state"] = (
            capo_tnb.types.nsd_operational_state.deserialize_json(
                data["nsdOperationalState"]
            )
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageOutput.nsd_operational_state required"
        )
    if data.get("nsdUsageState") is not None:
        import capo_tnb.types.nsd_usage_state

        out["nsd_usage_state"] = capo_tnb.types.nsd_usage_state.deserialize_json(
            data["nsdUsageState"]
        )
    else:
        raise DeserializationError(
            "GetSolNetworkPackageOutput.nsd_usage_state required"
        )
    if data.get("nsdId") is not None:
        out["nsd_id"] = data["nsdId"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.nsd_id required")
    if data.get("nsdName") is not None:
        out["nsd_name"] = data["nsdName"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.nsd_name required")
    if data.get("nsdVersion") is not None:
        out["nsd_version"] = data["nsdVersion"]
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.nsd_version required")
    if data.get("vnfPkgIds") is not None:
        import capo_tnb.types.vnf_pkg_id_list

        out["vnf_pkg_ids"] = capo_tnb.types.vnf_pkg_id_list.deserialize_json(
            data["vnfPkgIds"]
        )
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.vnf_pkg_ids required")
    if data.get("metadata") is not None:
        import capo_tnb.types.get_sol_network_package_metadata

        out["metadata"] = (
            capo_tnb.types.get_sol_network_package_metadata.deserialize_json(
                data["metadata"]
            )
        )
    else:
        raise DeserializationError("GetSolNetworkPackageOutput.metadata required")
    if data.get("tags") is not None:
        import capo_tnb.types.tag_map

        out["tags"] = capo_tnb.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetSolNetworkPackageOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
