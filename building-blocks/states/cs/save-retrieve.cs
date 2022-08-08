using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using Dapr.Client;
using Microsoft.AspNetCore.Mvc;
using System.Threading;
using System.Text.Json;



namespace EventService
{

    class Program
    {

        static async Task main(string args)
        {
            string DAPR_STORE_NAME = "statestore";

            while (true)
            {
                
                System.Threading.Thread.Sleep(5000);
                using var client = new DaprClientBuilder().Build();

                var random = new Random();

                var orderId = random.Next(1,1000);

                await client.SaveStateAsync(DAPR_STORE_NAME, "order_1", orderId.ToString());
                await client.SaveStateAsync(DAPR_STORE_NAME, "order_2", orderId.ToString());
                
                var result = await client.GetStateAsync<string>(DAPR_STORE_NAME, "order_1");
                Console.WriteLine("Result after get: " + result);

            }


        }
    }

}