using Npgsql;
using System.Data;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// Database Connection String (Docker network ke liye)
string connectionString = "Host=mubashir-db;Database=postgres;Username=postgres;Password=mubashir.105";

// --- ENDPOINT: View Tech News via .NET ---
app.MapGet("/api/banking-news", async () =>
{
    var newsList = new List<object>();
    using var conn = new NpgsqlConnection(connectionString);
    await conn.OpenAsync();

    using var cmd = new NpgsqlCommand("SELECT title, source, status FROM tech_news", conn);
    using var reader = await cmd.ExecuteReaderAsync();
    
    while (await reader.ReadAsync())
    {
        newsList.Add(new { 
            Title = reader.GetString(0), 
            Source = reader.GetString(1), 
            Status = reader.GetString(2) 
        });
    }

    return Results.Ok(new { System = "Mubashir .NET 9 Portal", Data = newsList });
});

app.Run();
