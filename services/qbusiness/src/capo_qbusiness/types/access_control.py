"""Generated from Smithy shape ``com.amazonaws.qbusiness#AccessControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.member_relation
    import capo_qbusiness.types.principals


class AccessControl(TypedDict, closed=True):
    principals: "capo_qbusiness.types.principals.Principals"
    """<p>Contains a list of principals, where a principal can be either a <code>USER</code> or a <code>GROUP</code>. Each principal can be have the following type of document access: <code>ALLOW</code> or <code>DENY</code>.</p>"""
    member_relation: NotRequired["capo_qbusiness.types.member_relation.MemberRelation"]
    """<p>Describes the member relation within a principal list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessControl) -> dict:
    out: dict = {}
    import capo_qbusiness.types.principals

    out["principals"] = capo_qbusiness.types.principals.serialize_json(
        value["principals"]
    )
    if "member_relation" in value:
        import capo_qbusiness.types.member_relation

        out["memberRelation"] = capo_qbusiness.types.member_relation.serialize_json(
            value["member_relation"]
        )
    return out


def deserialize_json(data: dict) -> AccessControl:
    out: AccessControl = {}  # type: ignore[typeddict-item]
    if data.get("principals") is not None:
        import capo_qbusiness.types.principals

        out["principals"] = capo_qbusiness.types.principals.deserialize_json(
            data["principals"]
        )
    else:
        out["principals"] = []
    if data.get("memberRelation") is not None:
        import capo_qbusiness.types.member_relation

        out["member_relation"] = capo_qbusiness.types.member_relation.deserialize_json(
            data["memberRelation"]
        )
    return out
