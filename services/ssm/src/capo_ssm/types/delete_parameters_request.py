"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameter_name_list


class DeleteParametersRequest(TypedDict, closed=True):
    names: "capo_ssm.types.parameter_name_list.ParameterNameList"
    """<p>The names of the parameters to delete. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParametersRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.parameter_name_list

    out["Names"] = capo_ssm.types.parameter_name_list.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParametersRequest:
    out: DeleteParametersRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_ssm.types.parameter_name_list

        out["names"] = capo_ssm.types.parameter_name_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    else:
        out["names"] = []
    return out
