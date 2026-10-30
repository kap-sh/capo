"""Generated from Smithy shape ``com.amazonaws.continuum#RepositoryName``."""

from typing import TypeAlias

"""The name of a repository in owner/repository format (e.g. acme/payments-api). For an organization-scoped integration, the owner segment must match the integration's GitHub organization (validated at environment creation time). For a personal-account integration, the owner segment is the personal GitHub username and is not validated."""
RepositoryName: TypeAlias = str
