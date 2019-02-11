db.adminCommand(
  {
    createUser: "rasa",
    pwd: "cdVbmVHARju9YfAPp2RGfwjwEudBYXw",
    roles: [{ role: "readWrite", db: "rasa" }],
    authenticationRestrictions: [
      {
        clientSource: ["172.20.0.0/24"]
      }
    ]
  }
)