using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using RandomNameGeneratorLibrary;

namespace aztagsync.api.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AppMetadataController : ControllerBase
    {
        private static readonly string[] Ids = new[]
        {
            "ea7bb249-5b65-4dea-88c8-15e5aa530fb7", "034cd59b-8363-4f3b-9879-d61e7bcd508e", "351d47b7-5a91-4925-9d60-300d42f4dbbe"
        };

        private readonly ILogger<AppMetadataController> _logger;

        public AppMetadataController(ILogger<AppMetadataController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<AppMetadata> Get()
        {
            return Ids.Select(i => new AppMetadata
            {
                Id = i,
                BusinessOwner = new PersonNameGenerator().GenerateRandomFirstAndLastName(),
                TechOwner = new PersonNameGenerator().GenerateRandomFirstAndLastName()
            });
        }
    }
}
