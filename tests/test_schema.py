from graphene.test import Client
from graphene_sandbox.data import get_query_count

from graphene_sandbox.schema import schema


def test_deep_query_avoids_n_plus_1_queries_problem():
    start_query_count = get_query_count()

    client = Client(schema=schema)
    executed = client.execute(
        """
{
  me {
    name
    bestFriend {
      name
    }
    friends {
      name
      bestFriend {
        name
      }
    }
  }
}
"""
    )
    assert executed == {
        "data": {
            "me": {
                "bestFriend": {"name": "Bob"},
                "friends": [
                    {"bestFriend": {"name": "Me"}, "name": "Bob"},
                    {"bestFriend": {"name": "Dee"}, "name": "Cal"},
                ],
                "name": "Me",
            }
        }
    }

    end_query_count = get_query_count()
    # The naive number of queries is 5:
    # - get_person(Me)
    # - get_person(Bob)
    # - get_friends(Me)
    # - get_person(Me)
    # - get_person(Dee)
    # We want to do better by removing the N+1 query problem, while still
    # producing the same result.
    assert end_query_count - start_query_count < 5
