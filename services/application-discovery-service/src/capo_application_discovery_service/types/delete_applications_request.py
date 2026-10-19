"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeleteApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.application_ids_list


class DeleteApplicationsRequest(TypedDict, closed=True):
    configuration_ids: "capo_application_discovery_service.types.application_ids_list.ApplicationIdsList"
    """<p>Configuration ID of an application to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationsRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.application_ids_list

    out["configurationIds"] = (
        capo_application_discovery_service.types.application_ids_list.serialize_aws_json_1_1(
            value["configuration_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationsRequest:
    out: DeleteApplicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("configurationIds") is not None:
        import capo_application_discovery_service.types.application_ids_list

        out["configuration_ids"] = (
            capo_application_discovery_service.types.application_ids_list.deserialize_aws_json_1_1(
                data["configurationIds"]
            )
        )
    else:
        out["configuration_ids"] = []
    return out
