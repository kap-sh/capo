"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetApplicationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.applications_list


class BatchGetApplicationsInput(TypedDict, closed=True):
    application_names: "capo_codedeploy.types.applications_list.ApplicationsList"
    """<p>A list of application names separated by spaces. The maximum number of application names you can specify is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetApplicationsInput) -> dict:
    out: dict = {}
    import capo_codedeploy.types.applications_list

    out["applicationNames"] = (
        capo_codedeploy.types.applications_list.serialize_aws_json_1_1(
            value["application_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetApplicationsInput:
    out: BatchGetApplicationsInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationNames") is not None:
        import capo_codedeploy.types.applications_list

        out["application_names"] = (
            capo_codedeploy.types.applications_list.deserialize_aws_json_1_1(
                data["applicationNames"]
            )
        )
    else:
        out["application_names"] = []
    return out
