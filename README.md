# The Brain of NoobSocial

The social media platform [NoobSocial](https://github.com/newtoallofthis123/NoobSocial) is written using Golang, HTMX and Templ.
However, I recently decided that I want to experiment with feed generation for the platform and I would need to do it in order:

1.Collect Data from user interactions

- [x] For the data to be meaningful, each post should be tagged and act as a unique data point.
- [x] The data should be tokenizable and embeddings should be generated for each content
- [ ] User likes, comments and views should be stored and treated as data points

2.Users can follow other users

3.Figure out a feed generation algorithm

- [ ] The feed should be generated based on the user's interests
- [ ] Interactions and user preferences should be taken into account
- [ ] The feed should be generated in real-time
- [ ] Followed users' posts should be prioritized

4.Implement a Search: Vector or Text based

- [ ] The search should be able to search for posts, users and tags
- [ ] The search should be able to search for similar posts

Well I have no idea how to do most of this, but I'm excited to learn and experiment with it.

## The Plan

NoobSocial as a platform will be developed independently and the brain will be integrated as an optional microservice.
This means that the brain can be used as a standalone service for other platforms as well.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
