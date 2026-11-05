"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DefaultAmiList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.default_ami

DefaultAmiList: TypeAlias = list["capo_elastic_beanstalk.types.default_ami.DefaultAmi"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DefaultAmiList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.default_ami

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.default_ami.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DefaultAmiList:
    import capo_elastic_beanstalk.types.default_ami

    out: DefaultAmiList = []
    for child in el.findall("member"):
        out.append(capo_elastic_beanstalk.types.default_ami.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DefaultAmiList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.default_ami

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.default_ami.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DefaultAmiList:
    import capo_elastic_beanstalk.types.default_ami

    out: DefaultAmiList = []
    for child in parent.findall(tag):
        out.append(capo_elastic_beanstalk.types.default_ami.deserialize_query(child))
    return out
