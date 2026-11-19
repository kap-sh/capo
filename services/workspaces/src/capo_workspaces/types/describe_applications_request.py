"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.compute_list
    import capo_workspaces.types.limit
    import capo_workspaces.types.operating_system_name_list
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.work_space_application_id_list
    import capo_workspaces.types.work_space_application_license_type
    import capo_workspaces.types.work_space_application_owner


class DescribeApplicationsRequest(TypedDict, closed=True):
    application_ids: NotRequired[
        "capo_workspaces.types.work_space_application_id_list.WorkSpaceApplicationIdList"
    ]
    """<p>The identifiers of one or more applications.</p>"""
    compute_type_names: NotRequired["capo_workspaces.types.compute_list.ComputeList"]
    """<p>The compute types supported by the applications.</p>"""
    license_type: NotRequired[
        "capo_workspaces.types.work_space_application_license_type.WorkSpaceApplicationLicenseType"
    ]
    """<p>The license availability for the applications.</p>"""
    operating_system_names: NotRequired[
        "capo_workspaces.types.operating_system_name_list.OperatingSystemNameList"
    ]
    """<p>The operating systems supported by the applications.</p>"""
    owner: NotRequired[
        "capo_workspaces.types.work_space_application_owner.WorkSpaceApplicationOwner"
    ]
    """<p>The owner of the applications.</p>"""
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of applications to return.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationsRequest) -> dict:
    out: dict = {}
    if "application_ids" in value:
        import capo_workspaces.types.work_space_application_id_list

        out["ApplicationIds"] = (
            capo_workspaces.types.work_space_application_id_list.serialize_aws_json_1_1(
                value["application_ids"]
            )
        )
    if "compute_type_names" in value:
        import capo_workspaces.types.compute_list

        out["ComputeTypeNames"] = (
            capo_workspaces.types.compute_list.serialize_aws_json_1_1(
                value["compute_type_names"]
            )
        )
    if "license_type" in value:
        import capo_workspaces.types.work_space_application_license_type

        out["LicenseType"] = (
            capo_workspaces.types.work_space_application_license_type.serialize_aws_json_1_1(
                value["license_type"]
            )
        )
    if "operating_system_names" in value:
        import capo_workspaces.types.operating_system_name_list

        out["OperatingSystemNames"] = (
            capo_workspaces.types.operating_system_name_list.serialize_aws_json_1_1(
                value["operating_system_names"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationsRequest:
    out: DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIds") is not None:
        import capo_workspaces.types.work_space_application_id_list

        out["application_ids"] = (
            capo_workspaces.types.work_space_application_id_list.deserialize_aws_json_1_1(
                data["ApplicationIds"]
            )
        )
    if data.get("ComputeTypeNames") is not None:
        import capo_workspaces.types.compute_list

        out["compute_type_names"] = (
            capo_workspaces.types.compute_list.deserialize_aws_json_1_1(
                data["ComputeTypeNames"]
            )
        )
    if data.get("LicenseType") is not None:
        import capo_workspaces.types.work_space_application_license_type

        out["license_type"] = (
            capo_workspaces.types.work_space_application_license_type.deserialize_aws_json_1_1(
                data["LicenseType"]
            )
        )
    if data.get("OperatingSystemNames") is not None:
        import capo_workspaces.types.operating_system_name_list

        out["operating_system_names"] = (
            capo_workspaces.types.operating_system_name_list.deserialize_aws_json_1_1(
                data["OperatingSystemNames"]
            )
        )
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeApplicationsRequest) -> dict:
    out: dict = {}
    if "application_ids" in value:
        import capo_workspaces.types.work_space_application_id_list

        out["ApplicationIds"] = (
            capo_workspaces.types.work_space_application_id_list.serialize_cbor(
                value["application_ids"]
            )
        )
    if "compute_type_names" in value:
        import capo_workspaces.types.compute_list

        out["ComputeTypeNames"] = capo_workspaces.types.compute_list.serialize_cbor(
            value["compute_type_names"]
        )
    if "license_type" in value:
        import capo_workspaces.types.work_space_application_license_type

        out["LicenseType"] = (
            capo_workspaces.types.work_space_application_license_type.serialize_cbor(
                value["license_type"]
            )
        )
    if "operating_system_names" in value:
        import capo_workspaces.types.operating_system_name_list

        out["OperatingSystemNames"] = (
            capo_workspaces.types.operating_system_name_list.serialize_cbor(
                value["operating_system_names"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeApplicationsRequest:
    out: DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIds") is not None:
        import capo_workspaces.types.work_space_application_id_list

        out["application_ids"] = (
            capo_workspaces.types.work_space_application_id_list.deserialize_cbor(
                data["ApplicationIds"]
            )
        )
    if data.get("ComputeTypeNames") is not None:
        import capo_workspaces.types.compute_list

        out["compute_type_names"] = capo_workspaces.types.compute_list.deserialize_cbor(
            data["ComputeTypeNames"]
        )
    if data.get("LicenseType") is not None:
        import capo_workspaces.types.work_space_application_license_type

        out["license_type"] = (
            capo_workspaces.types.work_space_application_license_type.deserialize_cbor(
                data["LicenseType"]
            )
        )
    if data.get("OperatingSystemNames") is not None:
        import capo_workspaces.types.operating_system_name_list

        out["operating_system_names"] = (
            capo_workspaces.types.operating_system_name_list.deserialize_cbor(
                data["OperatingSystemNames"]
            )
        )
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
