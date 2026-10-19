"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.bounded_environment_id_list


class DescribeEnvironmentsRequest(TypedDict, closed=True):
    environment_ids: (
        "capo_cloud9.types.bounded_environment_id_list.BoundedEnvironmentIdList"
    )
    """<p>The IDs of individual environments to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentsRequest) -> dict:
    out: dict = {}
    import capo_cloud9.types.bounded_environment_id_list

    out["environmentIds"] = (
        capo_cloud9.types.bounded_environment_id_list.serialize_aws_json_1_1(
            value["environment_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentsRequest:
    out: DescribeEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentIds") is not None:
        import capo_cloud9.types.bounded_environment_id_list

        out["environment_ids"] = (
            capo_cloud9.types.bounded_environment_id_list.deserialize_aws_json_1_1(
                data["environmentIds"]
            )
        )
    else:
        out["environment_ids"] = []
    return out
