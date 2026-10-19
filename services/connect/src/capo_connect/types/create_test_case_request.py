"""Generated from Smithy shape ``com.amazonaws.connect#CreateTestCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.test_case_content
    import capo_connect.types.test_case_description
    import capo_connect.types.test_case_entry_point
    import capo_connect.types.test_case_id
    import capo_connect.types.test_case_initialization_data
    import capo_connect.types.test_case_name
    import capo_connect.types.test_case_status
    import capo_connect.types.timestamp


class CreateTestCaseRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    name: "capo_connect.types.test_case_name.TestCaseName"
    """<p>The name of the test.</p>"""
    description: NotRequired[
        "capo_connect.types.test_case_description.TestCaseDescription"
    ]
    """<p>The description of the test.</p>"""
    content: "capo_connect.types.test_case_content.TestCaseContent"
    """<p>The JSON string that represents the content of the test.</p>"""
    entry_point: NotRequired[
        "capo_connect.types.test_case_entry_point.TestCaseEntryPoint"
    ]
    """<p>Defines the starting point for your test.</p>"""
    initialization_data: NotRequired[
        "capo_connect.types.test_case_initialization_data.TestCaseInitializationData"
    ]
    """<p>Defines the initial custom attributes for your test.</p>"""
    status: NotRequired["capo_connect.types.test_case_status.TestCaseStatus"]
    """<p>Indicates the test status as either SAVED or PUBLISHED. The PUBLISHED status will initiate validation on the content. The SAVED status does not initiate validation of the content.</p>"""
    test_case_id: NotRequired["capo_connect.types.test_case_id.TestCaseId"]
    """<p>Id of the test case if you want to create it in a replica region using Amazon Connect Global Resiliency</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The time at which the resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region in which the resource was last modified</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTestCaseRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Content"] = value["content"]
    if "entry_point" in value:
        import capo_connect.types.test_case_entry_point

        out["EntryPoint"] = capo_connect.types.test_case_entry_point.serialize_json(
            value["entry_point"]
        )
    if "initialization_data" in value:
        out["InitializationData"] = value["initialization_data"]
    if "status" in value:
        import capo_connect.types.test_case_status

        out["Status"] = capo_connect.types.test_case_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTestCaseRequest:
    out: CreateTestCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("EntryPoint") is not None:
        import capo_connect.types.test_case_entry_point

        out["entry_point"] = capo_connect.types.test_case_entry_point.deserialize_json(
            data["EntryPoint"]
        )
    if data.get("InitializationData") is not None:
        out["initialization_data"] = data["InitializationData"]
    if data.get("Status") is not None:
        import capo_connect.types.test_case_status

        out["status"] = capo_connect.types.test_case_status.deserialize_json(
            data["Status"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
