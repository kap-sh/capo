"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#MaxCountRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.boxed_boolean
    import capo_elastic_beanstalk.types.boxed_int


class MaxCountRule(TypedDict, closed=True):
    enabled: "capo_elastic_beanstalk.types.boxed_boolean.BoxedBoolean"
    """<p>Specify <code>true</code> to apply the rule, or <code>false</code> to disable it.</p>"""
    max_count: NotRequired["capo_elastic_beanstalk.types.boxed_int.BoxedInt"]
    """<p>Specify the maximum number of application versions to retain.</p>"""
    delete_source_from_s3: NotRequired[
        "capo_elastic_beanstalk.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Set to <code>true</code> to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MaxCountRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "max_count" in value:
        pairs.append((f"{key_prefix}MaxCount", str(value["max_count"])))
    if "delete_source_from_s3" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteSourceFromS3",
                "true" if value["delete_source_from_s3"] else "false",
            )
        )


def deserialize_query(el: Element) -> MaxCountRule:
    out: MaxCountRule = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_max_count = el.find("MaxCount")
    if child_max_count is not None:
        out["max_count"] = int(child_max_count.text or "")
    child_delete_source_from_s3 = el.find("DeleteSourceFromS3")
    if child_delete_source_from_s3 is not None:
        out["delete_source_from_s3"] = (
            child_delete_source_from_s3.text or ""
        ).lower() == "true"
    return out
