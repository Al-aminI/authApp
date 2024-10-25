# Django + GraphQL Project

This project is a Django application integrated with GraphQL.

## Models

The application consists of two primary models:

1. **User**
2. **Posts**

### User Authentication

- Users can create an account and log in to the system.
- Upon successful login, a JWT token will be returned.
- The JWT token is required for authentication before any action can be performed in the system. If the user is not authenticated with the JWT token, they will be unable to access any functionality.

### Database

- The application uses SQLite3 as the default database.
- A PostgreSQL database setup has also been initiated for production use.

## Testing with GraphQL Playground

You can test the GraphQL API using the following mutations:

1. **Create User**

```graphql
mutation {
  createUser(
    username: "ai"
    email: "ai@gmail.com"
    password: "P@55w0rd"
    bio: "This is my bio"
  ) {
    success
    user {
      id
      username
      email
    }
    errors
  }
}
