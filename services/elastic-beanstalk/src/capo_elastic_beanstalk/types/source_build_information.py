"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SourceBuildInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.source_location
    import capo_elastic_beanstalk.types.source_repository
    import capo_elastic_beanstalk.types.source_type


class SourceBuildInformation(TypedDict, closed=True):
    source_type: "capo_elastic_beanstalk.types.source_type.SourceType"
    """<p>The type of repository.</p> <ul> <li> <p> <code>Git</code> </p> </li> <li> <p> <code>Zip</code> </p> </li> </ul>"""
    source_repository: "capo_elastic_beanstalk.types.source_repository.SourceRepository"
    """<p>Location where the repository is stored.</p> <ul> <li> <p> <code>CodeCommit</code> </p> </li> <li> <p> <code>S3</code> </p> </li> </ul>"""
    source_location: "capo_elastic_beanstalk.types.source_location.SourceLocation"
    """<p>The location of the source code, as a formatted string, depending on the value of <code>SourceRepository</code> </p> <ul> <li> <p>For <code>CodeCommit</code>, the format is the repository name and commit ID, separated by a forward slash. For example, <code>my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a</code>.</p> </li> <li> <p>For <code>S3</code>, the format is the S3 bucket name and object key, separated by a forward slash. For example, <code>my-s3-bucket/Folders/my-source-file</code>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceBuildInformation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_elastic_beanstalk.types.source_type

    capo_elastic_beanstalk.types.source_type.serialize_query(
        value["source_type"], pairs, f"{key_prefix}SourceType"
    )
    import capo_elastic_beanstalk.types.source_repository

    capo_elastic_beanstalk.types.source_repository.serialize_query(
        value["source_repository"], pairs, f"{key_prefix}SourceRepository"
    )
    pairs.append((f"{key_prefix}SourceLocation", str(value["source_location"])))


def deserialize_query(el: Element) -> SourceBuildInformation:
    out: SourceBuildInformation = {}  # type: ignore[typeddict-item]
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import capo_elastic_beanstalk.types.source_type

        out["source_type"] = capo_elastic_beanstalk.types.source_type.deserialize_query(
            child_source_type
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_elastic_beanstalk.types.source_type.SourceType", ""
        )
    child_source_repository = el.find("SourceRepository")
    if child_source_repository is not None:
        import capo_elastic_beanstalk.types.source_repository

        out["source_repository"] = (
            capo_elastic_beanstalk.types.source_repository.deserialize_query(
                child_source_repository
            )
        )
    else:
        import typing

        out["source_repository"] = typing.cast(
            "capo_elastic_beanstalk.types.source_repository.SourceRepository", ""
        )
    child_source_location = el.find("SourceLocation")
    if child_source_location is not None:
        out["source_location"] = str(child_source_location.text or "")
    else:
        out["source_location"] = ""
    return out
