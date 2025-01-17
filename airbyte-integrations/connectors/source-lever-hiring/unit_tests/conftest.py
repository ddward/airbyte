#
# MIT License
#
# Copyright (c) 2020 Airbyte
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from pytest import fixture


@fixture
def test_config():
    return {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret",
        "refresh_token": "test_refresh_token",
        "environment": "Sandbox",
        "start_date": "2021-05-07T00:00:00Z",
    }


@fixture
def test_full_refresh_config():
    return {"base_url": "test_base_url"}


@fixture
def test_incremental_config():
    return {"base_url": "test_base_url", "start_date": "2020-01-01T00:00:00Z"}


@fixture
def test_opportunity_record():
    return {
        "id": "test_id",
        "name": "test_name",
        "contact": "test_contact",
        "headline": "test_headline",
        "stage": "test_stage",
        "confidentiality": "non-confidential",
        "location": "test_location",
        "phones": [{"type": "test_mobile", "value": "test_value"}],
        "emails": ["test_emails"],
        "links": ["test_link_1", "test_link_2"],
        "archived": {"reason": "test_reason", "archivedAt": 1628513942512},
        "tags": [],
        "sources": ["test_source_1"],
        "stageChanges": [{"toStageId": "test_lead-new", "toStageIndex": 0, "updatedAt": 1628509001183, "userId": "test_userId"}],
        "origin": "test_origin",
        "sourcedBy": "test_sourcedBy",
        "owner": "test_owner",
        "followers": ["test_follower"],
        "applications": ["test_application"],
        "createdAt": 1738509001183,
        "updatedAt": 1738542849132,
        "lastInteractionAt": 1738513942512,
        "lastAdvancedAt": 1738513942512,
        "snoozedUntil": None,
        "urls": {"list": "https://hire.sandbox.lever.co/candidates", "show": "https://hire.sandbox.lever.co/candidates/test_show"},
        "isAnonymized": False,
        "dataProtection": None,
    }
