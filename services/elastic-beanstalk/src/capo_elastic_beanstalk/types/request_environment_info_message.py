"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#RequestEnvironmentInfoMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_info_type
    import capo_elastic_beanstalk.types.environment_name


class RequestEnvironmentInfoMessage(TypedDict, closed=True):
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment of the requested data.</p> <p>If no such environment is found, <code>RequestEnvironmentInfo</code> returns an <code>InvalidParameterValue</code> error. </p> <p>Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment of the requested data.</p> <p>If no such environment is found, <code>RequestEnvironmentInfo</code> returns an <code>InvalidParameterValue</code> error. </p> <p>Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, Elastic Beanstalk returns <code>MissingRequiredParameter</code> error. </p>"""
    info_type: "capo_elastic_beanstalk.types.environment_info_type.EnvironmentInfoType"
    """<p>The type of information to request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RequestEnvironmentInfoMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environment_id" in value:
        pairs.append((f"{key_prefix}EnvironmentId", str(value["environment_id"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    import capo_elastic_beanstalk.types.environment_info_type

    capo_elastic_beanstalk.types.environment_info_type.serialize_query(
        value["info_type"], pairs, f"{key_prefix}InfoType"
    )


def deserialize_query(el: Element) -> RequestEnvironmentInfoMessage:
    out: RequestEnvironmentInfoMessage = {}  # type: ignore[typeddict-item]
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_info_type = el.find("InfoType")
    if child_info_type is not None:
        import capo_elastic_beanstalk.types.environment_info_type

        out["info_type"] = (
            capo_elastic_beanstalk.types.environment_info_type.deserialize_query(
                child_info_type
            )
        )
    else:
        import typing

        out["info_type"] = typing.cast(
            "capo_elastic_beanstalk.types.environment_info_type.EnvironmentInfoType", ""
        )
    return out
