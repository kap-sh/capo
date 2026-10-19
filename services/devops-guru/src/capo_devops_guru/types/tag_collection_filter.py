"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagCollectionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.app_boundary_key
    import capo_devops_guru.types.tag_values


class TagCollectionFilter(TypedDict, closed=True):
    app_boundary_key: "capo_devops_guru.types.app_boundary_key.AppBoundaryKey"
    """<p>An Amazon Web Services tag <i>key</i> that is used to identify the Amazon Web Services resources that DevOps Guru analyzes. All Amazon Web Services resources in your account and Region tagged with this <i>key</i> make up your DevOps Guru application and analysis boundary.</p> <important> <p>The string used for a <i>key</i> in a tag that you use to define your resource coverage must begin with the prefix <code>Devops-guru-</code>. The tag <i>key</i> might be <code>DevOps-Guru-deployment-application</code> or <code>devops-guru-rds-application</code>. When you create a <i>key</i>, the case of characters in the <i>key</i> can be whatever you choose. After you create a <i>key</i>, it is case-sensitive. For example, DevOps Guru works with a <i>key</i> named <code>devops-guru-rds</code> and a <i>key</i> named <code>DevOps-Guru-RDS</code>, and these act as two different <i>keys</i>. Possible <i>key</i>/<i>value</i> pairs in your application might be <code>Devops-Guru-production-application/RDS</code> or <code>Devops-Guru-production-application/containers</code>.</p> </important>"""
    tag_values: "capo_devops_guru.types.tag_values.TagValues"
    """<p>The values in an Amazon Web Services tag collection.</p> <p>The tag's <i>value</i> is an optional field used to associate a string with the tag <i>key</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). The <i>key</i> and <i>value</i> are the tag's <i>key</i> pair. Omitting the tag <i>value</i> is the same as using an empty string. Like tag <i>keys</i>, tag <i>values</i> are case-sensitive. You can specify a maximum of 256 characters for a tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagCollectionFilter) -> dict:
    out: dict = {}
    out["AppBoundaryKey"] = value["app_boundary_key"]
    import capo_devops_guru.types.tag_values

    out["TagValues"] = capo_devops_guru.types.tag_values.serialize_json(
        value["tag_values"]
    )
    return out


def deserialize_json(data: dict) -> TagCollectionFilter:
    out: TagCollectionFilter = {}  # type: ignore[typeddict-item]
    if data.get("AppBoundaryKey") is not None:
        out["app_boundary_key"] = data["AppBoundaryKey"]
    else:
        out["app_boundary_key"] = ""
    if data.get("TagValues") is not None:
        import capo_devops_guru.types.tag_values

        out["tag_values"] = capo_devops_guru.types.tag_values.deserialize_json(
            data["TagValues"]
        )
    else:
        out["tag_values"] = []
    return out
