import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  interface Post {
    account: {
      display_name: string;
      username: string;
      avatar: string;
      url: string;
    };
    content: string;
    media_attachments: {
      url: string;
      description: string;
    }[];
  }

  const [data, setData] = useState<Post[]>([]); // Start with an empty array
  const [refresh, setRefresh] = useState(false);

  useEffect(() => {
    console.log("Fetching data...");
    fetch('http://127.0.0.1:5000/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(resdata => {
        setData(resdata);
        console.log("Fetched data:", resdata);
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  }, [refresh]);

  return (
    <>
      <div>
        <button className="bg-[#]" onClick={() => {
          setRefresh(!refresh);
          console.log("Refreshed");
        }}>Refresh</button>
        <h1>Mastodon Recommender</h1>
        {data.map((post, index) => (
          <div key={index} className="post">
            <div className="flex">
              <img className="h-14 rounded-xl mr-3" src={post.account.avatar} alt={post.account.display_name} />
              <div className="flex flex-col items-start">
                <a href={post.account.url}>{post.account.display_name}</a>
                <h2>@{post.account.username}</h2>
              </div>
            </div>
            <div dangerouslySetInnerHTML={{ __html: post.content }} />
            {post.media_attachments.length > 0 && (
              <div>
                <h3>Media:</h3>
                {post.media_attachments.map((media, mediaIndex) => (
                  <div key={mediaIndex}>
                    <img src={media.url} alt={media.description} />
                    <p>{media.description}</p>
                  </div>
                ))}
              </div>
            )}
            <p><a href={post.account.url}>View Profile</a></p>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
