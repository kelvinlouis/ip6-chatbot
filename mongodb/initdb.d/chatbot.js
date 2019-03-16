db.adminCommand(
  {
    createUser: "chatbot",
    pwd: "MjEjkXFmzwTC28uKhj48wRwsYTsNGqb",
    roles: [{ role: "readWrite", db: "chatbot" }],
    authenticationRestrictions: [
      {
        clientSource: ["172.20.0.0/24"]
      }
    ]
  }
)